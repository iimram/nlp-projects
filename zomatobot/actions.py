from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'north indian':50,'south indian':85}		
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price_lowerlimit = tracker.get_slot('price_lowerlimit')
		price_upperlimit = tracker.get_slot('price_upperlimit')
		config={ "user_key":"b25791047f9c600c20fb110ef227c313"}
		zomato = zomatopy.initialize_app(config)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine.lower())),50)
		d = json.loads(results)
		if d['results_found'] > 0:
			response=formatMessageForChat(d,price_lowerlimit,price_upperlimit)
			emailresponse=formatMessageForEmail(d, price_lowerlimit, price_upperlimit)
		else :
			emailresponse = ""
			response = ""

		if emailresponse == "" :
			return [SlotSet('email_response',None), SlotSet('price_lowerlimit',None), SlotSet('price_upperlimit',None), SlotSet('location',None), SlotSet('cuisine',None)]
		else:
			dispatcher.utter_message("="*30 + " LUCKY YOU! HERE IS WHAT I FOUND " + "="*30 +"\n\n"+response)
			return [SlotSet('email_response',emailresponse)]

def formatMessageForChat(d, price_lowerlimit, price_upperlimit):
	msgFormat = color.BOLD +color.DARKCYAN + "{0}:  {1} " + color.END + "in {2} has been rated " + color.BOLD +color.DARKCYAN +" {3}.\n" + color.END 
	response = ""
	response = prepareCustomMessage(d,price_lowerlimit,price_upperlimit,msgFormat,5,'chat')
	if response == "":
		response = ""
		return response
	else:
		response = response + '='*100
		response = response + '\nBon Appetit!'
		return response

def formatMessageForEmail(d, price_lowerlimit, price_upperlimit):
	msgFormat = "<BR><B>Restaurant Name:</B> {0}<BR><B>Restaurant locality address:</B> {1}<BR><B>Average budget for two people:</B> {2}<BR><B>Zomato user rating:</B> {3}<BR><BR>"
	response = ""
	response = prepareCustomMessage(d,price_lowerlimit,price_upperlimit,msgFormat,10,'email')
	if response == "":
		response = ""
		return response
	else:	
		response = response + '='*30
		response = response + '<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR>'
		response = response + '<i>(This is an automatically generated email. Please do not reply. For any support please contact <b>support@foodie.com)</b></i>'
		return response

def prepareCustomMessage(d,price_lowerlimit, price_upperlimit,msgFormat,noOfRes,msgSource):
	count = 0
	response = ""
	if d['results_found'] == 0:
		response= "no results"
	elif ((price_lowerlimit==None) & (price_upperlimit==None)):
		for restaurant in d['restaurants']:
			if count < noOfRes:
				price = restaurant['restaurant']['average_cost_for_two']
				count = count + 1
				response=response + prepareEmailOrChatMsg(count,msgSource,restaurant,price,msgFormat)	
	elif ((price_lowerlimit==None) & (price_upperlimit!=None)):
		for restaurant in d['restaurants']:
			if count < noOfRes:
				price = restaurant['restaurant']['average_cost_for_two']					
				if (price > int(price_upperlimit)):
					count = count + 1
					response=response + prepareEmailOrChatMsg(count,msgSource,restaurant,price,msgFormat)	
	elif ((price_lowerlimit!=None) & (price_upperlimit==None)):
		for restaurant in d['restaurants']:
			if count < noOfRes:
				price = restaurant['restaurant']['average_cost_for_two']
				if (price < int(price_lowerlimit)):
					count = count + 1
					response=response + prepareEmailOrChatMsg(count,msgSource,restaurant,price,msgFormat)	
	elif ((price_lowerlimit!=None) & (price_upperlimit!=None)):
		for restaurant in d['restaurants']:
			if count < noOfRes:
				price = restaurant['restaurant']['average_cost_for_two'] 
				if ((price > int(price_lowerlimit)) & (price < int(price_upperlimit))):
					count = count + 1
					response=response + prepareEmailOrChatMsg(count,msgSource,restaurant,price,msgFormat)	
	return response

def prepareEmailOrChatMsg(resNumber, msgSource,restaurant,price,msgFormat):
	formattedMsg = ""
	if msgSource == 'chat':
		formattedMsg = msgFormat.format(resNumber,restaurant['restaurant']['name'], restaurant['restaurant']['location']['address'], restaurant['restaurant']['user_rating']['aggregate_rating'])
	elif msgSource == 'email':
		formattedMsg = msgFormat.format(restaurant['restaurant']['name'], restaurant['restaurant']['location']['address'], price, restaurant['restaurant']['user_rating']['aggregate_rating'])
	
	return formattedMsg

class ActionSendEmail(Action):
	def name(self):
		return 'action_sendemail'
		
	def run(self, dispatcher, tracker, domain):
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls() 
		hostEmail = "upgradnlpuser@gmail.com"
		s.login(hostEmail, "nlpuser123") 
		message = tracker.get_slot('email_response')
		toemail = tracker.get_slot('email_id')
		# print('sending email to', toemail)
		loc = tracker.get_slot('location')
		cui = tracker.get_slot('cuisine')
		cui = cui.capitalize()
		loc = loc.capitalize()

		subject = 'Subject: {}\n'.format("Hey Foodie!! Top " + cui + " restaurants in " + loc)
		# emailContent = 'Subject: {}\n\n{}'.format("Top " + cui + " Restaurants in " + loc, message)
		msg = MIMEMultipart('alternative')
		msg['Subject'] = subject
		msg['From'] = hostEmail
		msg['To'] = toemail

		text = subject
		html = """\
		<html>
		<body>
		Hi Foodie!<br>
		Hungry? Here are some fabulous restaurants you asked for.<br><br>
		""" + "="*30 + """
		""" + "<BR>" + """
		""" + message + """
		</body>
		</html>
		"""

		part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')

		msg.attach(part1)
		msg.attach(part2)

		s.sendmail(hostEmail, toemail, msg.as_string()) 
		s.quit()
		#response = message
		#dispatcher.utter_message("-----"+response)

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validatelocation'
		
	def run(self,disatcher,tracker,domain):
		self.tier1_tier2_cities = []
		f = open('tier1_tier2_cities.txt')
		for city in f.read().split():
			self.tier1_tier2_cities.append(city)
		city = tracker.get_slot('location')
		if city.lower() in self.tier1_tier2_cities:
			return [SlotSet('city_match','match')]
		else:
			return [SlotSet('city_match','notmatch'), SlotSet('location',None)]

class color:
   WHITE = '\037[40m'
   DARKCYAN = '\033[36m'
   BOLD = '\033[1m'
   END = '\033[0m'
		