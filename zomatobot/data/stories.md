## Generated Story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_validatelocation
	- slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
	- slot{"price_lowerlimit": "300"}
    - action_restaurant
	- utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* emailid_provided{"email_id": "iashfaq@outlook.com"}
	- slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
	- utter_email_sent
	- utter_goodbye
    - export

## Generated Story 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gulbarga"}
    - slot{"location": "gulbarga"}
	- action_validatelocation
	- slot{"city_match": "notmatch"}
	- utter_not_match_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_validatelocation
	- slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
	- slot{"price_lowerlimit": "300"}
    - action_restaurant
	- utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* emailid_provided{"email_id": "iashfaq@outlook.com"}
	- slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
	- utter_email_sent
	- utter_goodbye
    - export
	
## Generated Story 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_validatelocation
	- slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
	- slot{"price_upperlimit": "700"}
    - action_restaurant
	- utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* emailid_provided{"email_id": "iashfaq@outlook.com"}
	- slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
	- utter_email_sent
	- utter_goodbye
    - export

## Generated Story 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gulbarga"}
    - slot{"location": "gulbarga"}
	- action_validatelocation
	- slot{"city_match": "notmatch"}
	- utter_not_match_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
	- action_validatelocation
	- slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
	- slot{"price_upperlimit": "700"}
    - action_restaurant
	- utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* emailid_provided{"email_id": "iashfaq@outlook.com"}
	- slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
	- utter_email_sent
	- utter_goodbye
    - export

	## Generated Story 5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_validatelocation
	- slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
	- slot{"price_lowerlimit": "300"}
	- slot{"price_upperlimit": "700"}
    - action_restaurant
	- utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* emailid_provided{"email_id": "iashfaq@outlook.com"}
	- slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
	- utter_email_sent
	- utter_goodbye
    - export

## Generated Story 6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gulbarga"}
    - slot{"location": "gulbarga"}
	- action_validatelocation
	- slot{"city_match": "notmatch"}
	- utter_not_match_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
	- action_validatelocation
	- slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
	- slot{"price_lowerlimit": "300"}
	- slot{"price_upperlimit": "700"}
    - action_restaurant
	- utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* emailid_provided{"email_id": "iashfaq@outlook.com"}
	- slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
	- utter_email_sent
	- utter_goodbye
    - export

## Generated Story -2035636599385104215
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* emailid_provided{"email_id": "iashfaq@outlook.com"}
    - slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export
	
## Generated Story -2035636599385104215
* greet
    - utter_greet
* restaurant_search{"location": "gulbarga"}
    - slot{"location": "gulbarga"}
    - action_validatelocation
    - slot{"city_match": "notmatch"}
	- utter_not_match_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
	- action_validatelocation
	- slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* emailid_provided{"email_id": "iashfaq@outlook.com"}
    - slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -4219008339389652826
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - slot{"email_response": ""}
    - utter_no_result_price
    - utter_goodbye
    - export

## Generated Story 4223751264463724909
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "chennai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "chennai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - slot{"email_response": ""}
    - utter_no_result_price
    - utter_goodbye
    - export

## Generated Story -3003947235203207048
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Nasi And Mee\nRestaurant locality address: 66/6539, 2nd Floor, Narayanan Seva Sangam Building, Mullassery Canal Road, Shenoys, Kochi\nAverage budget for two people: 1000\nZomato user rating: 4.8\n\nRestaurant Name: Paragon\nRestaurant locality address: F 82-83, Level 1, LuLu Mall, NH-17, Entrance Road, Edapally Junction, Edappally, Kochi\nAverage budget for two people: 900\nZomato user rating: 4.5\n\nRestaurant Name: The Asian Kitchen by Tokyo Bay\nRestaurant locality address: Cochin Club, Opposite Parade Ground, St. Francis Church Road, Fort Kochi, Kochi\nAverage budget for two people: 1100\nZomato user rating: 4.5\n\nRestaurant Name: Grand Hotel Restaurant\nRestaurant locality address: Grand Hotel, MG Road, Kochi\nAverage budget for two people: 1000\nZomato user rating: 4.3\n\nRestaurant Name: Mainland China - Radisson Blue Kochi\nRestaurant locality address: Radisson Blue Kochi, Sahodaran Ayyappan Road, Elamkulam Junction, Elamkulam, Kochi\nAverage budget for two people: 1500\nZomato user rating: 4.2\n\nRestaurant Name: Latest Recipe - Le M\u00e9ridien Kochi\nRestaurant locality address: Maradu, Kochi, Kerala 682304\nAverage budget for two people: 2200\nZomato user rating: 4.2\n\nRestaurant Name: Wok & Grill\nRestaurant locality address: Near Gold Souk (200 Meters),Aysha Road,Kochi Bypass, Vyttila, Kochi\nAverage budget for two people: 1100\nZomato user rating: 4.1\n\nRestaurant Name: Chopstix\nRestaurant locality address: Seaport Airport Road, Ernakulam, Kakkanad, Kochi\nAverage budget for two people: 800\nZomato user rating: 4.1\n\nRestaurant Name: Chopstix\nRestaurant locality address: Civil Lane Road, Palarivattom, Kochi\nAverage budget for two people: 800\nZomato user rating: 4.1\n\n"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "iim.ram@gmail.com"}
    - slot{"email_id": "iim.ram@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -3257646809923229230
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "prayagraj"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "prayagraj"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Moti Mahal Delux Tandoori Trail\nRestaurant locality address: Shop 18A, Second Floor, Sardar Patel Marg, Above HDFC Bank, Civil Lines, Allahabad\nAverage budget for two people: 800\nZomato user rating: 3.8\n\n"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "iim.ram@gmail.com"}
    - slot{"email_id": "iim.ram@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -3206971625490517840
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* send_email{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Cream Centre\nRestaurant locality address: 128/180, Orbit Avenue, Thirugnanasambandam Road, Opposite Bishop Appasamy College, Gopalapuram, Race Course, Coimbatore\nAverage budget for two people: 1000\nZomato user rating: 4.3\n\nRestaurant Name: Bird On Tree\nRestaurant locality address: 28, Opposite Circuit House, Behind HDFC, Race Course, Coimbatore\nAverage budget for two people: 1200\nZomato user rating: 4.3\n\nRestaurant Name: Balle Balle\nRestaurant locality address: 30, Bharathi Park ,Second Cross, Saibaba Colony, Coimbatore\nAverage budget for two people: 1000\nZomato user rating: 4.2\n\nRestaurant Name: The Cascade Restaurant\nRestaurant locality address: 479-B1, Avinashi Road, Near Suguna Kalyana Mandapam, Peelamedu, Coimbatore\nAverage budget for two people: 1200\nZomato user rating: 4.2\n\nRestaurant Name: My Place Restaurant\nRestaurant locality address: 744/2, New Damu Nagar, Puliakulam, Near Ramanathapuram, Ramanathapuram, Coimbatore\nAverage budget for two people: 800\nZomato user rating: 4.2\n\n"}
    - utter_ask_to_send_mail
* send_email{"email_id": "iim.ram@gmail.com"}
    - slot{"email_id": "iim.ram@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 1935128870139925507
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "madurai"}
    - slot{"location": "madurai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Johnny Dony\nRestaurant locality address: 103 South Marret Street, Periyar, Madurai\nAverage budget for two people: 200\nZomato user rating: 4.3\n\nRestaurant Name: Rohit Fast Foods\nRestaurant locality address: 98, Valluvar Colony Main Road Pillaiyar Kovil Opp Madurai -625014, Viswanathapuram, Madurai\nAverage budget for two people: 200\nZomato user rating: 4.2\n\nRestaurant Name: Famous Jigarthanda\nRestaurant locality address: 43, Inside Thiyagarajan Automobiles Indian Oil Petrol Bunk, Alagarkoil Road, Tallakulam, KK Nagar, Madurai\nAverage budget for two people: 200\nZomato user rating: 4.0\n\nRestaurant Name: Johnny Dony\nRestaurant locality address: 12A. Subramania Pillai Street, SS Colony, Madurai\nAverage budget for two people: 200\nZomato user rating: 4.0\n\nRestaurant Name: Savage\nRestaurant locality address: Walking Path, KK Nagar, Madurai\nAverage budget for two people: 250\nZomato user rating: 4.0\n\nRestaurant Name: Bell Jumbo Restaurant\nRestaurant locality address: Sammatipuram, Arrapalayam, Madurai\nAverage budget for two people: 200\nZomato user rating: 3.9\n\nRestaurant Name: Sree Mohan Bhojanalay\nRestaurant locality address: 33, Dhanappa Mudali Street, West Town Street, Periyar, Madurai\nAverage budget for two people: 150\nZomato user rating: 3.9\n\nRestaurant Name: Zam Zam shawarma\nRestaurant locality address: 141, North Veli Street, Yanaikal Periyar, Madurai\nAverage budget for two people: 250\nZomato user rating: 3.8\n\nRestaurant Name: Grab N Grill\nRestaurant locality address: Mahatma Gandhi Nagar, Viswanathapuram, Madurai\nAverage budget for two people: 200\nZomato user rating: 3.8\n\nRestaurant Name: Star Broilers\nRestaurant locality address: Krishnnagar Colony, Viswanathapuram, Madurai\nAverage budget for two people: 250\nZomato user rating: 3.8\n\n"}
    - utter_ask_to_send_mail
* send_email{"email_id": "mahagopi.ram@gmail.com"}
    - slot{"email_id": "mahagopi.ram@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 5296665944008629788
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "thiruvananthapuram"}
    - slot{"location": "thiruvananthapuram"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: The Egg Stop\nRestaurant locality address: Near Brand Factory, Keston Road, Ambalamukku, Trivandrum\nAverage budget for two people: 250\nZomato user rating: 0\n\nRestaurant Name: Chicking\nRestaurant locality address: Polayathode, Kollam Circle, Kovalam, Trivandrum\nAverage budget for two people: 200\nZomato user rating: 0\n\nRestaurant Name: Fusion Flavours Restaurant \nRestaurant locality address: 2nd Floor, Kedaram Complex, Vivekanand Nagar, Kesavadasapuram, Trivandrum\nAverage budget for two people: 200\nZomato user rating: 0\n\n"}
    - utter_ask_to_send_mail
* goodbye
    - utter_goodbye
    - export

## Generated Story -2163231102643127502
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* send_email{"location": "tenkasi"}
    - slot{"location": "tenkasi"}
    - action_validatelocation
    - slot{"city_match": "notmatch"}
    - slot{"location": null}
    - utter_not_match_location
* restaurant_search{"location": "tirunelveli"}
    - slot{"location": "tirunelveli"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": null}
    - utter_no_result_price
    - utter_goodbye
    - export

## Generated Story 2962003924693843247
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Byg Brewski Brewing Company\nRestaurant locality address: Behind MK Retail, Sarjapur Road, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.9\n\nRestaurant Name: The Boozy Griffin\nRestaurant locality address: 20/7, 4th & 5th Floor, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\nAverage budget for two people: 1800\nZomato user rating: 4.8\n\nRestaurant Name: ECHOES Koramangala\nRestaurant locality address: Shop 44, 4th B Cross Road, Koramangala 5th Block, Bangalore\nAverage budget for two people: 750\nZomato user rating: 4.8\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: 2nd Floor, Orion Mall, Dr. Rajkumar Road, Malleshwaram, Bangalore\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: Biergarten\nRestaurant locality address: 4th B Cross, Koramangala 5th Block, Bangalore\nAverage budget for two people: 2100\nZomato user rating: 4.7\n\nRestaurant Name: ShakesBierre\nRestaurant locality address: Level 5, Eva Mall, Brigade Road, Bangalore\nAverage budget for two people: 1500\nZomato user rating: 4.7\n\nRestaurant Name: Byg Brewski Brewing Company\nRestaurant locality address: 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.7\n\nRestaurant Name: TBC Sky Lounge\nRestaurant locality address: Astra Hotel, 2795, 27th Main, Sector 1, HSR, Bangalore\nAverage budget for two people: 1000\nZomato user rating: 4.7\n\nRestaurant Name: Brew and Barbeque - A Microbrewery Pub\nRestaurant locality address: 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\nAverage budget for two people: 1400\nZomato user rating: 4.7\n\nRestaurant Name: Truffles\nRestaurant locality address: 28, 4th 'B' Cross, Koramangala 5th Block, Bangalore\nAverage budget for two people: 900\nZomato user rating: 4.7\n\n"}
    - utter_ask_to_send_mail
* send_email{"email_id": "jyorajesh@gmail.com"}
    - slot{"email_id": "jyorajesh@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

###########################################################################################################################
###########################################################################################################################
## KOUSTUBH STORIES ##
## Generated Story -6748480406384626577
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search
    - action_validatelocation
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Coal Barbecues\nRestaurant locality address: 40, 2nd Floor, Bazullah Road, T. Nagar, Chennai\nAverage budget for two people: 1400\nZomato user rating: 4.9\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: 49 & 50 L, Express Avenue Mall, White's Road, Royapettah, Chennai\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: S-29, 2nd Floor, Phoneix Market City, 142, Velachery Main Road, Chennai\nAverage budget for two people: 1400\nZomato user rating: 4.7\n\nRestaurant Name: Sigree Global Grill\nRestaurant locality address: The Spring Hotel, Kodambakkam High Road, Nungambakkam, Chennai\nAverage budget for two people: 1200\nZomato user rating: 4.6\n\nRestaurant Name: Fromage\nRestaurant locality address: Somerset Greenway, Lords Avenue, MRC Nagar, Chennai\nAverage budget for two people: 1000\nZomato user rating: 4.5\n\nRestaurant Name: Mamagoto\nRestaurant locality address: Shop 9, Oyster Building, Khader Nawaz Khan Road, Nungambakkam, Chennai\nAverage budget for two people: 1500\nZomato user rating: 4.5\n\nRestaurant Name: Little Italy\nRestaurant locality address: E-50, 17th Cross Street, Lane Before Spencers Daily, Besant Nagar, Chennai\nAverage budget for two people: 1500\nZomato user rating: 4.5\n\nRestaurant Name: Amelie's\nRestaurant locality address: 6,Seshadri Road, Venus Colony, Alwarpet, Chennai\nAverage budget for two people: 900\nZomato user rating: 4.4\n\nRestaurant Name: Joker's Kitchen\nRestaurant locality address: 94/1, Door 211/1, TTK Road, Near Ethiraj Kalayana Mandapam, Alwarpet, Chennai\nAverage budget for two people: 800\nZomato user rating: 4.4\n\nRestaurant Name: Maplai\nRestaurant locality address: 14, Sterling Avenue, Nungambakkam, Chennai\nAverage budget for two people: 1000\nZomato user rating: 4.4\n\n"}
    - utter_ask_to_send_mail
    - utter_ask_to_send_mail
* send_email
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 1292799723869864554
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Byg Brewski Brewing Company\nRestaurant locality address: Behind MK Retail, Sarjapur Road, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.9\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: 100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.9\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.9\n\nRestaurant Name: Flechazo\nRestaurant locality address: 120 A3, 2nd Floor, Santosh Tower, EPIP Industrial Area, Phase 1, Hoodi Village, Whitefield, Bangalore\nAverage budget for two people: 1400\nZomato user rating: 4.9\n\nRestaurant Name: The Black Pearl\nRestaurant locality address: 105, 1st A Cross Road, Jyothi Nivas College Road, Koramangala 5th Block, Bangalore\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: The Globe Grub\nRestaurant locality address: 2nd Floor, Soul Space Paradigm, Above Bata Showroom, Outer Ring Road, Marathahalli, Bangalore\nAverage budget for two people: 1300\nZomato user rating: 4.8\n\nRestaurant Name: The Boozy Griffin\nRestaurant locality address: 20/7, 4th & 5th Floor, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\nAverage budget for two people: 1800\nZomato user rating: 4.8\n\nRestaurant Name: ECHOES Koramangala\nRestaurant locality address: Shop 44, 4th B Cross Road, Koramangala 5th Block, Bangalore\nAverage budget for two people: 750\nZomato user rating: 4.8\n\nRestaurant Name: Barbeque Nation\nRestaurant locality address: 67, 15th Cross, 6th B Main, JP Nagar, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.8\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: 2nd Floor, Orion Mall, Dr. Rajkumar Road, Malleshwaram, Bangalore\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\n"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -7380323723453651380
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Sentosa MultiCuisine Restaurant\nRestaurant locality address: Pune-Mumbai Expressway, Ravet, Pune\nAverage budget for two people: 1200\nZomato user rating: 4.9\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: Shop 206, 2nd Floor White Square Building, Opposite Atlanta Complex Hinjewadi, Hinjawadi, Pune\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: Shop 10, 11 & 12, Mariplex Mall, Kalyani Nagar, Pune\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: Royal China\nRestaurant locality address: Business Plaza Westin Hotel, KP Annexe, Mundhwa, Pune\nAverage budget for two people: 2500\nZomato user rating: 4.8\n\nRestaurant Name: Agent Jack's\nRestaurant locality address: West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\nAverage budget for two people: 1300\nZomato user rating: 4.7\n\nRestaurant Name: The Sassy Spoon\nRestaurant locality address: Lane 7, Sanskriti Lifestyle Complex, Koregaon Park, Pune\nAverage budget for two people: 1500\nZomato user rating: 4.7\n\nRestaurant Name: BarBerry\nRestaurant locality address: 121/122, Rambaug Colony, Next lane of MIT Collage, Opposite Kheliya Shop, Paud road, Kothrud, Pune\nAverage budget for two people: 1200\nZomato user rating: 4.7\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: 2nd Floor Seasons Mall, Magarpatta, Pune\nAverage budget for two people: 1400\nZomato user rating: 4.7\n\nRestaurant Name: Pop Tate's\nRestaurant locality address: Shop T08, 3rd floor, Phoenix Market City Mall, Viman Nagar, Pune\nAverage budget for two people: 1500\nZomato user rating: 4.7\n\n"}
    - utter_ask_to_send_mail
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "iim.ram@gmail.com"}
    - slot{"email_id": "iim.ram@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 5171569256140314238
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "\u001b[1mRestaurant Name:\u001b[0m Kebabs & Curries Company\n\u001b[1mRestaurant locality address:\u001b[0m World Trade Park, JLN Marg, Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 800\n\u001b[1mZomato user rating:\u001b[0m  4.9\n\n\u001b[1mRestaurant Name:\u001b[0m The Night Jar\n\u001b[1mRestaurant locality address:\u001b[0m 3rd Floor, Leisure Inn Grand Chanakya, Panch Batti, MI Road, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 2500\n\u001b[1mZomato user rating:\u001b[0m  4.8\n\n\u001b[1mRestaurant Name:\u001b[0m ta Blu - Hotel Clarks Amer\n\u001b[1mRestaurant locality address:\u001b[0m Hotel Clarks Amer, Jawaharlal Nehru Marg, Near Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1900\n\u001b[1mZomato user rating:\u001b[0m  4.8\n\n\u001b[1mRestaurant Name:\u001b[0m Skyfall By Replay\n\u001b[1mRestaurant locality address:\u001b[0m SB 57, 5th Floor, Ridhi Tower, Opposite SMS Stadium, Tonk Road, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1500\n\u001b[1mZomato user rating:\u001b[0m  4.7\n\n\u001b[1mRestaurant Name:\u001b[0m Sultanat\n\u001b[1mRestaurant locality address:\u001b[0m The Fort, P-20, Lal Bahadur, S.L Marg, Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1200\n\u001b[1mZomato user rating:\u001b[0m  4.7\n\n\u001b[1mRestaurant Name:\u001b[0m Caf\u00e9 Bae\n\u001b[1mRestaurant locality address:\u001b[0m Hotel Las Vegas, A1, 21 Sehkar Marg, Bais Godam, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1200\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\u001b[1mRestaurant Name:\u001b[0m Monarch Restaurant - Holiday Inn Jaipur City Centre\n\u001b[1mRestaurant locality address:\u001b[0m Holiday Inn Jaipur City Centre, Commercial Plot 1, Sardar Patel Road, Bais Godam, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1900\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\u001b[1mRestaurant Name:\u001b[0m Zoya\n\u001b[1mRestaurant locality address:\u001b[0m The Fort, P-20, Lal Bahadur, S.L Marg, Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1700\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\u001b[1mRestaurant Name:\u001b[0m Masala Ministry\n\u001b[1mRestaurant locality address:\u001b[0m A 25, Near Genpact, J.L.N. Road, Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 900\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\u001b[1mRestaurant Name:\u001b[0m Mojo's Irish Pub\n\u001b[1mRestaurant locality address:\u001b[0m Levels,Ramada Hotel, Avenue 1, Govind Marg, Raja Park, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1100\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 192349649853384351
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_restaurant
    - slot{"email_response": "\u001b[1m\u001b[36mRestaurant Name: \u001b[0mAB's - Absolute Barbecues\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChurrolto\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mFilm Nagar Main Road, In Front Of Indian Oil, Film Nagar, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1200\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mB-Dubs\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mPlot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mFeranoz P\u00e2tisserie & Caf\u00e8\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m8-2-542/V/8, Road 7, Banjara Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mThe Roastery Coffee House\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m800\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChili's American Grill & Bar\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mFlat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mCon\u00e7u\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mPlot no 738, Road no. 37, Jubilee Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChili's American Grill & Bar\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mF 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mFlechazo\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m2nd Floor, Sun Towers, Sector 1, Huda Techno Enclave, Above Mangatrai Jewellers, Madhapur, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1300\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mOver The Moon Brew Company\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mPlot B 2, Survey  6/1, Quiet Lands, Gachibowli, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1200\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 9048010032452079188
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "\u001b[1m\u001b[36mRestaurant Name: \u001b[0mTapri Central\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mB4 E, 3rd Floor, Surana Jewellers, Opposite Central Park, C Scheme, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m800\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mKebabs & Curries Company\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mWorld Trade Park, JLN Marg, Malviya Nagar, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m800\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mThe Night Jar\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m3rd Floor, Leisure Inn Grand Chanakya, Panch Batti, MI Road, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m2500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mMeraaki Kitchen\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m27, Madrampura, Civil Lines Metro Station, Opposite Pillar 88, Civil Lines, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mta Blu - Hotel Clarks Amer\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mHotel Clarks Amer, Jawaharlal Nehru Marg, Near Malviya Nagar, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1900\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mSkyfall By Replay\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mSB 57, 5th Floor, Ridhi Tower, Opposite SMS Stadium, Tonk Road, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChowk\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mThe Fort, P-20, Lal Bahadur, S.L Marg, Malviya Nagar, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m800\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mSultanat\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mThe Fort, P-20, Lal Bahadur, S.L Marg, Malviya Nagar, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1200\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mAkh Bar\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mFloor 6, Sarovar Premiere, Sahakar Marg, Tonk Road, Lal Kothi, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mLevels\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mRamada Hotel, Avenue 1, Govind Marg, Raja Park, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -4805112258247465553
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* send_email{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "\u001b[1m\u001b[36mRestaurant Name: \u001b[0mYaaran Da Adda\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mOpposite AIIMS Gate 5, Main Road, Tatibandh\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.3 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mCorn Bite\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mOutside City Center Mall, Devendra Nagar\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m350\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.2 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChefs Kitchen\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mShop 24  Highway Complex Bhagat Singh Chowk Telibandha Road, Civil Lines, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.1 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mGirnar Restaurant\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mJaistambh Chowk, GE Road, Raipur (CG)\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.1 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mNaivedya\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mJail Road, Raipur, Devendra Nagar, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.1 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mFood Villa\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mAshoka Ratan Compound, Vidhan Sabha, Shankar Nagar, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.1 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mHotel Hyderabadi\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mEvergreen Chowk, Madrasa Road, Bajinathpara, Moudhapara, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.0 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mIndian Coffee House\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mShyam Square Market, Pandri, Devendra Nagar Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.0 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mRamdev's Khana Khazana\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mHIG-3/1, Kachna Pahuch Marg, Geetanjali Colony, Shankar Nagar, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.0 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mMadrasi Bites\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mPandri Choti Lane, Opposite Adidas, Govind Nagar, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.0 \n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -2754920458020421835
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<B>Restaurant Name:</B> Hitchki<BR>Restaurant locality address: 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai\nAverage budget for two people: 1200\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Hitchki<BR>Restaurant locality address: Ground Floor, R City Mall, Ghatkopar West, Mumbai\nAverage budget for two people: 1200\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Angrezi Dhaba<BR>Restaurant locality address: 23/2 1st Floor, RM Building, Mahalaxmi Station Bridge, Dr. E Moses Road, Mahalaxmi, Mumbai\nAverage budget for two people: 1500\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Palladium Social<BR>Restaurant locality address: Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai\nAverage budget for two people: 1400\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> February 30<BR>Restaurant locality address: Shop 28, Ground Floor, Meera Co-Operative Housing Society Limited, Oshiwara Link Road, Opposite Mega Mall, Oshiwara, Andheri West, Mumbai\nAverage budget for two people: 2000\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Trumpet Sky Lounge<BR>Restaurant locality address: 2nd Floor, Dalia Estate, Off New Link Road, Near Fun Republic, Andheri Lokhandwala, Andheri West, Mumbai\nAverage budget for two people: 1700\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Rocky Star Cocktail Bar<BR>Restaurant locality address: Third Floor, Trade View Building, Kamala Mills Compound, Senapati Bapat Marg, Lower Parel, Mumbai\nAverage budget for two people: 1500\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Thirsty City 127<BR>Restaurant locality address: Todi Mills & Compund, Mathuradas Mill, Senapati Bapat Marg, Lower Parel, Mumbai\nAverage budget for two people: 2500\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Tamasha<BR>Restaurant locality address: Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai\nAverage budget for two people: 2700\nZomato user rating: 4.8\n\n<B>Restaurant Name:</B> Hitchki<BR>Restaurant locality address: 5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai\nAverage budget for two people: 1200\nZomato user rating: 4.8\n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -4317917866688617382
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<B>Restaurant Name:</B> Dana Choga<BR>Restaurant locality address: 5 & Amp; 6, Atul Kataria Chowk, Sector 14, Gurgaon<BR>Average budget for two people: 500<BR>Zomato user rating: 4.7<BR><BR>\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* goodbye
    - utter_goodbye
    - export

## Generated Story -4506907918907217023
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "pune"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - slot{"email_response": "\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* goodbye
    - utter_goodbye
    - export

## Generated Story 7351812770080662984
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "ahmedabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "ahmedabad"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<B>Restaurant Name:</B> Yanki Sizzlers<BR>Restaurant locality address: HL College Road, Opposite Naran Park Society, Commerce Six Roads, C G Road, Ahmedabad<BR>Average budget for two people: 1200<BR>Zomato user rating: 4.9<BR><BR><B>Restaurant Name:</B> Huber & Holly<BR>Restaurant locality address: 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad<BR>Average budget for two people: 800<BR>Zomato user rating: 4.8<BR><BR><B>Restaurant Name:</B> Lollo Rosso<BR>Restaurant locality address: 3, Ground Floor, One World Capital, Opposite Lane Of Orbit, Off Rajpath Rangoli Road, Bodakdev, Ahmedabad<BR>Average budget for two people: 900<BR>Zomato user rating: 4.8<BR><BR><B>Restaurant Name:</B> The Red Bistro<BR>Restaurant locality address: Armeida, Sindhu Bhavan Road, Off SG Road, Bodakdev, Ahmedabad<BR>Average budget for two people: 1400<BR>Zomato user rating: 4.6<BR><BR><B>Restaurant Name:</B> Nini's Kitchen<BR>Restaurant locality address: 104/105, First Floor, 3rd Eye Vision, Dr. Vikram Sarabhai Marg (IIM road), Near Nexa Showroom, Vastrapur, Ahmedabad<BR>Average budget for two people: 1000<BR>Zomato user rating: 4.6<BR><BR><B>Restaurant Name:</B> Tomato's<BR>Restaurant locality address: 1-3, Mardia Plaza, C G Road, Ahmedabad<BR>Average budget for two people: 1400<BR>Zomato user rating: 4.6<BR><BR><B>Restaurant Name:</B> Nini's Kitchen<BR>Restaurant locality address: 9C, Venus Atlantis, Near Shell Petrol Pump, Prahlad Nagar, Ahmedabad<BR>Average budget for two people: 1000<BR>Zomato user rating: 4.5<BR><BR><B>Restaurant Name:</B> La Patron Cafe<BR>Restaurant locality address: UGF 7, 8, 9, Vaishali Complex, Opposite Jade Blue, Lal Bangalow Cross Road, C G Road, Ahmedabad<BR>Average budget for two people: 800<BR>Zomato user rating: 4.5<BR><BR><B>Restaurant Name:</B> Ph Se Food<BR>Restaurant locality address: 205-206, Silve Radiance, Sindhu Bhawan Road, Pakwan Char Rasta, Bodakdev, Ahmedabad<BR>Average budget for two people: 900<BR>Zomato user rating: 4.4<BR><BR><B>Restaurant Name:</B> The Esplendido Cafe<BR>Restaurant locality address: Ground Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad<BR>Average budget for two people: 800<BR>Zomato user rating: 4.4<BR><BR><BR>==============================<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR><i>This is an automatically generated email. Please do not reply. For any support from team foddie, contact <b>support@foodie.com</b></i>"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

###########################################################################################################################
###########################################################################################################################

## Generated Story 7294808868409905286
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "bengaluru"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bengaluru"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": null}
    - slot{"price_lowerlimit": null}
    - slot{"price_upperlimit": null}
    - utter_no_result_price
    - utter_goodbye
    - export

## Generated Story -1431790506805246801
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "bengaluru"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "bengaluru"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<BR><B>Restaurant Name:</B> Byg Brewski Brewing Company<BR><B>Restaurant locality address:</B> Behind MK Retail, Sarjapur Road, Bangalore<BR><B>Average budget for two people:</B> 1600<BR><B>Zomato user rating:</B> 4.9<BR><BR><BR><B>Restaurant Name:</B> The Boozy Griffin<BR><B>Restaurant locality address:</B> 20/7, 4th & 5th Floor, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore<BR><B>Average budget for two people:</B> 1800<BR><B>Zomato user rating:</B> 4.8<BR><BR><BR><B>Restaurant Name:</B> ECHOES Koramangala<BR><B>Restaurant locality address:</B> Shop 44, 4th B Cross Road, Koramangala 5th Block, Bangalore<BR><B>Average budget for two people:</B> 750<BR><B>Zomato user rating:</B> 4.8<BR><BR><BR><B>Restaurant Name:</B> Chili's American Grill & Bar<BR><B>Restaurant locality address:</B> 2nd Floor, Orion Mall, Dr. Rajkumar Road, Malleshwaram, Bangalore<BR><B>Average budget for two people:</B> 1400<BR><B>Zomato user rating:</B> 4.8<BR><BR><BR><B>Restaurant Name:</B> Biergarten<BR><B>Restaurant locality address:</B> 4th B Cross, Koramangala 5th Block, Bangalore<BR><B>Average budget for two people:</B> 2100<BR><B>Zomato user rating:</B> 4.7<BR><BR><BR><B>Restaurant Name:</B> ShakesBierre<BR><B>Restaurant locality address:</B> Level 5, Eva Mall, Brigade Road, Bangalore<BR><B>Average budget for two people:</B> 1500<BR><B>Zomato user rating:</B> 4.7<BR><BR><BR><B>Restaurant Name:</B> Byg Brewski Brewing Company<BR><B>Restaurant locality address:</B> 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore<BR><B>Average budget for two people:</B> 1600<BR><B>Zomato user rating:</B> 4.7<BR><BR><BR><B>Restaurant Name:</B> TBC Sky Lounge<BR><B>Restaurant locality address:</B> Astra Hotel, 2795, 27th Main, Sector 1, HSR, Bangalore<BR><B>Average budget for two people:</B> 1000<BR><B>Zomato user rating:</B> 4.7<BR><BR><BR><B>Restaurant Name:</B> Truffles<BR><B>Restaurant locality address:</B> 28, 4th 'B' Cross, Koramangala 5th Block, Bangalore<BR><B>Average budget for two people:</B> 900<BR><B>Zomato user rating:</B> 4.7<BR><BR><BR><B>Restaurant Name:</B> Brew and Barbeque - A Microbrewery Pub<BR><B>Restaurant locality address:</B> 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore<BR><B>Average budget for two people:</B> 1400<BR><B>Zomato user rating:</B> 4.7<BR><BR>==============================<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR><i>(This is an automatically generated email. Please do not reply. For any support please contact <b>support@foodie.com)</b></i>"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "iim.ram@gmail.com"}
    - slot{"email_id": "iim.ram@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -8727169338700422907
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<BR><B>Restaurant Name:</B> Byg Brewski Brewing Company<BR><B>Restaurant locality address:</B> Behind MK Retail, Sarjapur Road, Bangalore<BR><B>Average budget for two people:</B> 1600<BR><B>Zomato user rating:</B> 4.9<BR><BR><BR><B>Restaurant Name:</B> AB's - Absolute Barbecues<BR><B>Restaurant locality address:</B> 100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore<BR><B>Average budget for two people:</B> 1600<BR><B>Zomato user rating:</B> 4.9<BR><BR><BR><B>Restaurant Name:</B> AB's - Absolute Barbecues<BR><B>Restaurant locality address:</B> 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore<BR><B>Average budget for two people:</B> 1600<BR><B>Zomato user rating:</B> 4.9<BR><BR><BR><B>Restaurant Name:</B> Asia Kitchen By Mainland China<BR><B>Restaurant locality address:</B> 136, Ground Floor, 1st Cross, 5th Block, Jyoti Niwas College Road, Koramangala 5th Block, Bangalore<BR><B>Average budget for two people:</B> 1500<BR><B>Zomato user rating:</B> 4.9<BR><BR><BR><B>Restaurant Name:</B> Flechazo<BR><B>Restaurant locality address:</B> 120 A3, 2nd Floor, Santosh Tower, EPIP Industrial Area, Phase 1, Hoodi Village, Whitefield, Bangalore<BR><B>Average budget for two people:</B> 1400<BR><B>Zomato user rating:</B> 4.9<BR><BR><BR><B>Restaurant Name:</B> The Black Pearl<BR><B>Restaurant locality address:</B> 105, 1st A Cross Road, Jyothi Nivas College Road, Koramangala 5th Block, Bangalore<BR><B>Average budget for two people:</B> 1400<BR><B>Zomato user rating:</B> 4.8<BR><BR><BR><B>Restaurant Name:</B> The Globe Grub<BR><B>Restaurant locality address:</B> 2nd Floor, Soul Space Paradigm, Above Bata Showroom, Outer Ring Road, Marathahalli, Bangalore<BR><B>Average budget for two people:</B> 1300<BR><B>Zomato user rating:</B> 4.8<BR><BR><BR><B>Restaurant Name:</B> The Boozy Griffin<BR><B>Restaurant locality address:</B> 20/7, 4th & 5th Floor, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore<BR><B>Average budget for two people:</B> 1800<BR><B>Zomato user rating:</B> 4.8<BR><BR><BR><B>Restaurant Name:</B> ECHOES Koramangala<BR><B>Restaurant locality address:</B> Shop 44, 4th B Cross Road, Koramangala 5th Block, Bangalore<BR><B>Average budget for two people:</B> 750<BR><B>Zomato user rating:</B> 4.8<BR><BR><BR><B>Restaurant Name:</B> Barbecue by Punjab Grill<BR><B>Restaurant locality address:</B> Unit T-1, Third Floor, Sampige Road, Mantri Square Mall, Malleshwaram, Bangalore<BR><B>Average budget for two people:</B> 1300<BR><B>Zomato user rating:</B> 4.8<BR><BR>==============================<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR><i>(This is an automatically generated email. Please do not reply. For any support please contact <b>support@foodie.com)</b></i>"}
    - utter_ask_to_send_mail
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "iim.ram@gmail.com"}
    - slot{"email_id": "iim.ram@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export


###########################################################################################################################
###########################################################################################################################
## KOUSTUBH STORIES ##
## Generated Story -6748480406384626577
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search
    - action_validatelocation
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Coal Barbecues\nRestaurant locality address: 40, 2nd Floor, Bazullah Road, T. Nagar, Chennai\nAverage budget for two people: 1400\nZomato user rating: 4.9\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: 49 & 50 L, Express Avenue Mall, White's Road, Royapettah, Chennai\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: S-29, 2nd Floor, Phoneix Market City, 142, Velachery Main Road, Chennai\nAverage budget for two people: 1400\nZomato user rating: 4.7\n\nRestaurant Name: Sigree Global Grill\nRestaurant locality address: The Spring Hotel, Kodambakkam High Road, Nungambakkam, Chennai\nAverage budget for two people: 1200\nZomato user rating: 4.6\n\nRestaurant Name: Fromage\nRestaurant locality address: Somerset Greenway, Lords Avenue, MRC Nagar, Chennai\nAverage budget for two people: 1000\nZomato user rating: 4.5\n\nRestaurant Name: Mamagoto\nRestaurant locality address: Shop 9, Oyster Building, Khader Nawaz Khan Road, Nungambakkam, Chennai\nAverage budget for two people: 1500\nZomato user rating: 4.5\n\nRestaurant Name: Little Italy\nRestaurant locality address: E-50, 17th Cross Street, Lane Before Spencers Daily, Besant Nagar, Chennai\nAverage budget for two people: 1500\nZomato user rating: 4.5\n\nRestaurant Name: Amelie's\nRestaurant locality address: 6,Seshadri Road, Venus Colony, Alwarpet, Chennai\nAverage budget for two people: 900\nZomato user rating: 4.4\n\nRestaurant Name: Joker's Kitchen\nRestaurant locality address: 94/1, Door 211/1, TTK Road, Near Ethiraj Kalayana Mandapam, Alwarpet, Chennai\nAverage budget for two people: 800\nZomato user rating: 4.4\n\nRestaurant Name: Maplai\nRestaurant locality address: 14, Sterling Avenue, Nungambakkam, Chennai\nAverage budget for two people: 1000\nZomato user rating: 4.4\n\n"}
    - utter_ask_to_send_mail
    - utter_ask_to_send_mail
* send_email
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 1292799723869864554
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Byg Brewski Brewing Company\nRestaurant locality address: Behind MK Retail, Sarjapur Road, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.9\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: 100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.9\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.9\n\nRestaurant Name: Flechazo\nRestaurant locality address: 120 A3, 2nd Floor, Santosh Tower, EPIP Industrial Area, Phase 1, Hoodi Village, Whitefield, Bangalore\nAverage budget for two people: 1400\nZomato user rating: 4.9\n\nRestaurant Name: The Black Pearl\nRestaurant locality address: 105, 1st A Cross Road, Jyothi Nivas College Road, Koramangala 5th Block, Bangalore\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: The Globe Grub\nRestaurant locality address: 2nd Floor, Soul Space Paradigm, Above Bata Showroom, Outer Ring Road, Marathahalli, Bangalore\nAverage budget for two people: 1300\nZomato user rating: 4.8\n\nRestaurant Name: The Boozy Griffin\nRestaurant locality address: 20/7, 4th & 5th Floor, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\nAverage budget for two people: 1800\nZomato user rating: 4.8\n\nRestaurant Name: ECHOES Koramangala\nRestaurant locality address: Shop 44, 4th B Cross Road, Koramangala 5th Block, Bangalore\nAverage budget for two people: 750\nZomato user rating: 4.8\n\nRestaurant Name: Barbeque Nation\nRestaurant locality address: 67, 15th Cross, 6th B Main, JP Nagar, Bangalore\nAverage budget for two people: 1600\nZomato user rating: 4.8\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: 2nd Floor, Orion Mall, Dr. Rajkumar Road, Malleshwaram, Bangalore\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\n"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -7380323723453651380
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "Restaurant Name: Sentosa MultiCuisine Restaurant\nRestaurant locality address: Pune-Mumbai Expressway, Ravet, Pune\nAverage budget for two people: 1200\nZomato user rating: 4.9\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: Shop 206, 2nd Floor White Square Building, Opposite Atlanta Complex Hinjewadi, Hinjawadi, Pune\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: Shop 10, 11 & 12, Mariplex Mall, Kalyani Nagar, Pune\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: Chili's American Grill & Bar\nRestaurant locality address: UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\nAverage budget for two people: 1400\nZomato user rating: 4.8\n\nRestaurant Name: Royal China\nRestaurant locality address: Business Plaza Westin Hotel, KP Annexe, Mundhwa, Pune\nAverage budget for two people: 2500\nZomato user rating: 4.8\n\nRestaurant Name: Agent Jack's\nRestaurant locality address: West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\nAverage budget for two people: 1300\nZomato user rating: 4.7\n\nRestaurant Name: The Sassy Spoon\nRestaurant locality address: Lane 7, Sanskriti Lifestyle Complex, Koregaon Park, Pune\nAverage budget for two people: 1500\nZomato user rating: 4.7\n\nRestaurant Name: BarBerry\nRestaurant locality address: 121/122, Rambaug Colony, Next lane of MIT Collage, Opposite Kheliya Shop, Paud road, Kothrud, Pune\nAverage budget for two people: 1200\nZomato user rating: 4.7\n\nRestaurant Name: AB's - Absolute Barbecues\nRestaurant locality address: 2nd Floor Seasons Mall, Magarpatta, Pune\nAverage budget for two people: 1400\nZomato user rating: 4.7\n\nRestaurant Name: Pop Tate's\nRestaurant locality address: Shop T08, 3rd floor, Phoenix Market City Mall, Viman Nagar, Pune\nAverage budget for two people: 1500\nZomato user rating: 4.7\n\n"}
    - utter_ask_to_send_mail
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "iim.ram@gmail.com"}
    - slot{"email_id": "iim.ram@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 5171569256140314238
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "\u001b[1mRestaurant Name:\u001b[0m Kebabs & Curries Company\n\u001b[1mRestaurant locality address:\u001b[0m World Trade Park, JLN Marg, Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 800\n\u001b[1mZomato user rating:\u001b[0m  4.9\n\n\u001b[1mRestaurant Name:\u001b[0m The Night Jar\n\u001b[1mRestaurant locality address:\u001b[0m 3rd Floor, Leisure Inn Grand Chanakya, Panch Batti, MI Road, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 2500\n\u001b[1mZomato user rating:\u001b[0m  4.8\n\n\u001b[1mRestaurant Name:\u001b[0m ta Blu - Hotel Clarks Amer\n\u001b[1mRestaurant locality address:\u001b[0m Hotel Clarks Amer, Jawaharlal Nehru Marg, Near Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1900\n\u001b[1mZomato user rating:\u001b[0m  4.8\n\n\u001b[1mRestaurant Name:\u001b[0m Skyfall By Replay\n\u001b[1mRestaurant locality address:\u001b[0m SB 57, 5th Floor, Ridhi Tower, Opposite SMS Stadium, Tonk Road, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1500\n\u001b[1mZomato user rating:\u001b[0m  4.7\n\n\u001b[1mRestaurant Name:\u001b[0m Sultanat\n\u001b[1mRestaurant locality address:\u001b[0m The Fort, P-20, Lal Bahadur, S.L Marg, Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1200\n\u001b[1mZomato user rating:\u001b[0m  4.7\n\n\u001b[1mRestaurant Name:\u001b[0m Caf\u00e9 Bae\n\u001b[1mRestaurant locality address:\u001b[0m Hotel Las Vegas, A1, 21 Sehkar Marg, Bais Godam, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1200\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\u001b[1mRestaurant Name:\u001b[0m Monarch Restaurant - Holiday Inn Jaipur City Centre\n\u001b[1mRestaurant locality address:\u001b[0m Holiday Inn Jaipur City Centre, Commercial Plot 1, Sardar Patel Road, Bais Godam, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1900\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\u001b[1mRestaurant Name:\u001b[0m Zoya\n\u001b[1mRestaurant locality address:\u001b[0m The Fort, P-20, Lal Bahadur, S.L Marg, Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1700\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\u001b[1mRestaurant Name:\u001b[0m Masala Ministry\n\u001b[1mRestaurant locality address:\u001b[0m A 25, Near Genpact, J.L.N. Road, Malviya Nagar, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 900\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\u001b[1mRestaurant Name:\u001b[0m Mojo's Irish Pub\n\u001b[1mRestaurant locality address:\u001b[0m Levels,Ramada Hotel, Avenue 1, Govind Marg, Raja Park, Jaipur\n\u001b[1mAverage budget for two people:\u001b[0m 1100\n\u001b[1mZomato user rating:\u001b[0m  4.6\n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 192349649853384351
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_restaurant
    - slot{"email_response": "\u001b[1m\u001b[36mRestaurant Name: \u001b[0mAB's - Absolute Barbecues\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChurrolto\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mFilm Nagar Main Road, In Front Of Indian Oil, Film Nagar, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1200\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mB-Dubs\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mPlot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mFeranoz P\u00e2tisserie & Caf\u00e8\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m8-2-542/V/8, Road 7, Banjara Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mThe Roastery Coffee House\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m800\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChili's American Grill & Bar\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mFlat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mCon\u00e7u\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mPlot no 738, Road no. 37, Jubilee Hills, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChili's American Grill & Bar\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mF 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mFlechazo\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m2nd Floor, Sun Towers, Sector 1, Huda Techno Enclave, Above Mangatrai Jewellers, Madhapur, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1300\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mOver The Moon Brew Company\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mPlot B 2, Survey  6/1, Quiet Lands, Gachibowli, Hyderabad\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1200\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 9048010032452079188
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "\u001b[1m\u001b[36mRestaurant Name: \u001b[0mTapri Central\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mB4 E, 3rd Floor, Surana Jewellers, Opposite Central Park, C Scheme, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m800\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mKebabs & Curries Company\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mWorld Trade Park, JLN Marg, Malviya Nagar, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m800\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.9\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mThe Night Jar\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m3rd Floor, Leisure Inn Grand Chanakya, Panch Batti, MI Road, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m2500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mMeraaki Kitchen\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0m27, Madrampura, Civil Lines Metro Station, Opposite Pillar 88, Civil Lines, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mta Blu - Hotel Clarks Amer\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mHotel Clarks Amer, Jawaharlal Nehru Marg, Near Malviya Nagar, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1900\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.8\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mSkyfall By Replay\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mSB 57, 5th Floor, Ridhi Tower, Opposite SMS Stadium, Tonk Road, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChowk\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mThe Fort, P-20, Lal Bahadur, S.L Marg, Malviya Nagar, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m800\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mSultanat\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mThe Fort, P-20, Lal Bahadur, S.L Marg, Malviya Nagar, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1200\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mAkh Bar\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mFloor 6, Sarovar Premiere, Sahakar Marg, Tonk Road, Lal Kothi, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mLevels\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mRamada Hotel, Avenue 1, Govind Marg, Raja Park, Jaipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m1600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.7\n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -4805112258247465553
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* send_email{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "\u001b[1m\u001b[36mRestaurant Name: \u001b[0mYaaran Da Adda\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mOpposite AIIMS Gate 5, Main Road, Tatibandh\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.3 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mCorn Bite\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mOutside City Center Mall, Devendra Nagar\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m350\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.2 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mChefs Kitchen\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mShop 24  Highway Complex Bhagat Singh Chowk Telibandha Road, Civil Lines, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.1 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mGirnar Restaurant\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mJaistambh Chowk, GE Road, Raipur (CG)\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.1 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mNaivedya\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mJail Road, Raipur, Devendra Nagar, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.1 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mFood Villa\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mAshoka Ratan Compound, Vidhan Sabha, Shankar Nagar, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m600\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.1 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mHotel Hyderabadi\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mEvergreen Chowk, Madrasa Road, Bajinathpara, Moudhapara, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.0 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mIndian Coffee House\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mShyam Square Market, Pandri, Devendra Nagar Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.0 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mRamdev's Khana Khazana\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mHIG-3/1, Kachna Pahuch Marg, Geetanjali Colony, Shankar Nagar, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m400\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.0 \n\n\u001b[1m\u001b[36mRestaurant Name: \u001b[0mMadrasi Bites\n\u001b[1m\u001b[36mRestaurant locality address: \u001b[0mPandri Choti Lane, Opposite Adidas, Govind Nagar, Raipur\n\u001b[1m\u001b[36mAverage budget for two people: \u001b[0m500\n\u001b[1m\u001b[36mZomato user rating:\u001b[0m4.0 \n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -2754920458020421835
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<B>Restaurant Name:</B> Hitchki<BR>Restaurant locality address: 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai\nAverage budget for two people: 1200\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Hitchki<BR>Restaurant locality address: Ground Floor, R City Mall, Ghatkopar West, Mumbai\nAverage budget for two people: 1200\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Angrezi Dhaba<BR>Restaurant locality address: 23/2 1st Floor, RM Building, Mahalaxmi Station Bridge, Dr. E Moses Road, Mahalaxmi, Mumbai\nAverage budget for two people: 1500\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Palladium Social<BR>Restaurant locality address: Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai\nAverage budget for two people: 1400\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> February 30<BR>Restaurant locality address: Shop 28, Ground Floor, Meera Co-Operative Housing Society Limited, Oshiwara Link Road, Opposite Mega Mall, Oshiwara, Andheri West, Mumbai\nAverage budget for two people: 2000\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Trumpet Sky Lounge<BR>Restaurant locality address: 2nd Floor, Dalia Estate, Off New Link Road, Near Fun Republic, Andheri Lokhandwala, Andheri West, Mumbai\nAverage budget for two people: 1700\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Rocky Star Cocktail Bar<BR>Restaurant locality address: Third Floor, Trade View Building, Kamala Mills Compound, Senapati Bapat Marg, Lower Parel, Mumbai\nAverage budget for two people: 1500\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Thirsty City 127<BR>Restaurant locality address: Todi Mills & Compund, Mathuradas Mill, Senapati Bapat Marg, Lower Parel, Mumbai\nAverage budget for two people: 2500\nZomato user rating: 4.9\n\n<B>Restaurant Name:</B> Tamasha<BR>Restaurant locality address: Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai\nAverage budget for two people: 2700\nZomato user rating: 4.8\n\n<B>Restaurant Name:</B> Hitchki<BR>Restaurant locality address: 5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai\nAverage budget for two people: 1200\nZomato user rating: 4.8\n\n\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -4317917866688617382
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<B>Restaurant Name:</B> Dana Choga<BR>Restaurant locality address: 5 & Amp; 6, Atul Kataria Chowk, Sector 14, Gurgaon<BR>Average budget for two people: 500<BR>Zomato user rating: 4.7<BR><BR>\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* goodbye
    - utter_goodbye
    - export

## Generated Story -4506907918907217023
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "pune"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - slot{"email_response": "\n====================================================================================================\nBon Appetit!"}
    - utter_ask_to_send_mail
* goodbye
    - utter_goodbye
    - export

## Generated Story 7351812770080662984
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "ahmedabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "ahmedabad"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<B>Restaurant Name:</B> Yanki Sizzlers<BR>Restaurant locality address: HL College Road, Opposite Naran Park Society, Commerce Six Roads, C G Road, Ahmedabad<BR>Average budget for two people: 1200<BR>Zomato user rating: 4.9<BR><BR><B>Restaurant Name:</B> Huber & Holly<BR>Restaurant locality address: 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad<BR>Average budget for two people: 800<BR>Zomato user rating: 4.8<BR><BR><B>Restaurant Name:</B> Lollo Rosso<BR>Restaurant locality address: 3, Ground Floor, One World Capital, Opposite Lane Of Orbit, Off Rajpath Rangoli Road, Bodakdev, Ahmedabad<BR>Average budget for two people: 900<BR>Zomato user rating: 4.8<BR><BR><B>Restaurant Name:</B> The Red Bistro<BR>Restaurant locality address: Armeida, Sindhu Bhavan Road, Off SG Road, Bodakdev, Ahmedabad<BR>Average budget for two people: 1400<BR>Zomato user rating: 4.6<BR><BR><B>Restaurant Name:</B> Nini's Kitchen<BR>Restaurant locality address: 104/105, First Floor, 3rd Eye Vision, Dr. Vikram Sarabhai Marg (IIM road), Near Nexa Showroom, Vastrapur, Ahmedabad<BR>Average budget for two people: 1000<BR>Zomato user rating: 4.6<BR><BR><B>Restaurant Name:</B> Tomato's<BR>Restaurant locality address: 1-3, Mardia Plaza, C G Road, Ahmedabad<BR>Average budget for two people: 1400<BR>Zomato user rating: 4.6<BR><BR><B>Restaurant Name:</B> Nini's Kitchen<BR>Restaurant locality address: 9C, Venus Atlantis, Near Shell Petrol Pump, Prahlad Nagar, Ahmedabad<BR>Average budget for two people: 1000<BR>Zomato user rating: 4.5<BR><BR><B>Restaurant Name:</B> La Patron Cafe<BR>Restaurant locality address: UGF 7, 8, 9, Vaishali Complex, Opposite Jade Blue, Lal Bangalow Cross Road, C G Road, Ahmedabad<BR>Average budget for two people: 800<BR>Zomato user rating: 4.5<BR><BR><B>Restaurant Name:</B> Ph Se Food<BR>Restaurant locality address: 205-206, Silve Radiance, Sindhu Bhawan Road, Pakwan Char Rasta, Bodakdev, Ahmedabad<BR>Average budget for two people: 900<BR>Zomato user rating: 4.4<BR><BR><B>Restaurant Name:</B> The Esplendido Cafe<BR>Restaurant locality address: Ground Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad<BR>Average budget for two people: 800<BR>Zomato user rating: 4.4<BR><BR><BR>==============================<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR><i>This is an automatically generated email. Please do not reply. For any support from team foddie, contact <b>support@foodie.com</b></i>"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "koustubh.klkpvn@gmail.com"}
    - slot{"email_id": "koustubh.klkpvn@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 7294808868409905286
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "bengaluru"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bengaluru"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": null}
    - slot{"price_lowerlimit": null}
    - slot{"price_upperlimit": null}
    - utter_no_result_price
    - utter_goodbye
    - export

###########################################################################################################################
###########################################################################################################################

## Generated Story -8185773534285107578
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "pune"}
    - slot{"cuisine": "american"}
    - slot{"location": "pune"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<BR><B>Restaurant Name:</B> Anda Ground<BR><B>Restaurant locality address:</B> Shop A1, Sai Heritage, Near Medipoint Hospital, Aundh, Pune<BR><B>Average budget for two people:</B> 400<BR><B>Zomato user rating:</B> 4.7<BR><BR>==============================<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR><i>(This is an automatically generated email. Please do not reply. For any support please contact <b>support@foodie.com)</b></i>"}
    - utter_ask_to_send_mail
* goodbye
    - utter_goodbye
    - export

## Generated Story 3442626622557358769 Illiyas story1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": null}
    - slot{"price_lowerlimit": null}
    - slot{"price_upperlimit": null}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "iashfaq@outlook.com"}
    - slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export
	
## Generated Story -357969707535465269 Illiyas story2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300", "price_upperlimit": "700"}
    - slot{"price_lowerlimit": "300"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": null}
    - slot{"price_lowerlimit": null}
    - slot{"price_upperlimit": null}
    - utter_ask_to_send_mail
* send_email{"email_id": "iashfaq@outlook.com"}
    - slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -1217156989120102982 Illiyas story3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<BR><B>Restaurant Name:</B> Hitchki<BR><B>Restaurant locality address:</B> 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai<BR><B>Average budget for two people:</B> 1200<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Angrezi Dhaba<BR><B>Restaurant locality address:</B> 23/2 1st Floor, RM Building, Mahalaxmi Station Bridge, Dr. E Moses Road, Mahalaxmi, Mumbai<BR><B>Average budget for two people:</B> 1500<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Hitchki<BR><B>Restaurant locality address:</B> Ground Floor, R City Mall, Ghatkopar West, Mumbai<BR><B>Average budget for two people:</B> 1200<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Trumpet Sky Lounge<BR><B>Restaurant locality address:</B> 2nd Floor, Dalia Estate, Off New Link Road, Near Fun Republic, Andheri Lokhandwala, Andheri West, Mumbai<BR><B>Average budget for two people:</B> 1700<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> February 30<BR><B>Restaurant locality address:</B> Shop 28, Ground Floor, Meera Co-Operative Housing Society Limited, Oshiwara Link Road, Opposite Mega Mall, Oshiwara, Andheri West, Mumbai<BR><B>Average budget for two people:</B> 2000<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Rocky Star Cocktail Bar<BR><B>Restaurant locality address:</B> Third Floor, Trade View Building, Kamala Mills Compound, Senapati Bapat Marg, Lower Parel, Mumbai<BR><B>Average budget for two people:</B> 1500<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Global Quarters<BR><B>Restaurant locality address:</B> Unit 1, A- Wing, Kailash Business Park, Parksite, Vikhroli, Mumbai<BR><B>Average budget for two people:</B> 1500<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Thirsty City 127<BR><B>Restaurant locality address:</B> Todi Mills & Compund, Mathuradas Mill, Senapati Bapat Marg, Lower Parel, Mumbai<BR><B>Average budget for two people:</B> 2500<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Tamasha<BR><B>Restaurant locality address:</B> Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai<BR><B>Average budget for two people:</B> 2700<BR><B>Zomato user rating:</B> 4.8<BR><BR><B>Restaurant Name:</B> Hitchki<BR><B>Restaurant locality address:</B> 5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai<BR><B>Average budget for two people:</B> 1200<BR><B>Zomato user rating:</B> 4.8<BR>==============================<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR><i>(This is an automatically generated email. Please do not reply. For any support please contact <b>support@foodie.com)</b></i>"}
    - utter_ask_to_send_mail
* send_email{"email_id": "iashfaq@outlook.com"}
    - slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -1217156989120102982 Illiyas story4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<BR><B>Restaurant Name:</B> Hitchki<BR><B>Restaurant locality address:</B> 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai<BR><B>Average budget for two people:</B> 1200<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Angrezi Dhaba<BR><B>Restaurant locality address:</B> 23/2 1st Floor, RM Building, Mahalaxmi Station Bridge, Dr. E Moses Road, Mahalaxmi, Mumbai<BR><B>Average budget for two people:</B> 1500<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Hitchki<BR><B>Restaurant locality address:</B> Ground Floor, R City Mall, Ghatkopar West, Mumbai<BR><B>Average budget for two people:</B> 1200<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Trumpet Sky Lounge<BR><B>Restaurant locality address:</B> 2nd Floor, Dalia Estate, Off New Link Road, Near Fun Republic, Andheri Lokhandwala, Andheri West, Mumbai<BR><B>Average budget for two people:</B> 1700<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> February 30<BR><B>Restaurant locality address:</B> Shop 28, Ground Floor, Meera Co-Operative Housing Society Limited, Oshiwara Link Road, Opposite Mega Mall, Oshiwara, Andheri West, Mumbai<BR><B>Average budget for two people:</B> 2000<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Rocky Star Cocktail Bar<BR><B>Restaurant locality address:</B> Third Floor, Trade View Building, Kamala Mills Compound, Senapati Bapat Marg, Lower Parel, Mumbai<BR><B>Average budget for two people:</B> 1500<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Global Quarters<BR><B>Restaurant locality address:</B> Unit 1, A- Wing, Kailash Business Park, Parksite, Vikhroli, Mumbai<BR><B>Average budget for two people:</B> 1500<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Thirsty City 127<BR><B>Restaurant locality address:</B> Todi Mills & Compund, Mathuradas Mill, Senapati Bapat Marg, Lower Parel, Mumbai<BR><B>Average budget for two people:</B> 2500<BR><B>Zomato user rating:</B> 4.9<BR><BR><B>Restaurant Name:</B> Tamasha<BR><B>Restaurant locality address:</B> Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai<BR><B>Average budget for two people:</B> 2700<BR><B>Zomato user rating:</B> 4.8<BR><BR><B>Restaurant Name:</B> Hitchki<BR><B>Restaurant locality address:</B> 5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai<BR><B>Average budget for two people:</B> 1200<BR><B>Zomato user rating:</B> 4.8<BR>==============================<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR><i>(This is an automatically generated email. Please do not reply. For any support please contact <b>support@foodie.com)</b></i>"}
    - utter_ask_to_send_mail
* affirm
    - utter_ask_emailid
* send_email{"email_id": "iashfaq@outlook.com"}
    - slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -4745925564091141843 Illiyas story5
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validatelocation
    - slot{"city_match": "notmatch"}
    - slot{"location": null}
    - utter_not_match_location
* restaurant_search{"location": "allahbad"}
    - slot{"location": "allahbad"}
    - action_validatelocation
    - slot{"city_match": "notmatch"}
    - slot{"location": null}
    - utter_not_match_location
* restaurant_search{"location": "prayagraj"}
    - slot{"location": "prayagraj"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_upperlimit": "700"}
    - slot{"price_upperlimit": "700"}
    - action_restaurant
    - slot{"email_response": "<BR><B>Restaurant Name:</B> EDEN by Connoisseur<BR><B>Restaurant locality address:</B> Hotel Samrat, Civil Lines, Allahabad<BR><B>Average budget for two people:</B> 1000<BR><B>Zomato user rating:</B> 4.6<BR><BR><BR><B>Restaurant Name:</B> Old School Cafe<BR><B>Restaurant locality address:</B> 33/2/A, Stretchy Road, Civil Lines, Allahabad<BR><B>Average budget for two people:</B> 1000<BR><B>Zomato user rating:</B> 4.5<BR><BR><BR><B>Restaurant Name:</B> El Chico Restaurant<BR><B>Restaurant locality address:</B> 142A, 32, Mahatma Gandhi, Civil Lines, Allahabad<BR><B>Average budget for two people:</B> 800<BR><B>Zomato user rating:</B> 4.3<BR><BR><BR><B>Restaurant Name:</B> Moti Mahal Delux<BR><B>Restaurant locality address:</B> Second Floor, Vinayak City Center Mall, SP Marg, Civil Lines, Allahabad<BR><B>Average budget for two people:</B> 850<BR><B>Zomato user rating:</B> 4.0<BR><BR><BR><B>Restaurant Name:</B> Relish Restaurant- The Legend Hotel<BR><B>Restaurant locality address:</B> The Legend Hotel, First Floor, 23 C, Thornhill Road, Civil Lines, Allahabad<BR><B>Average budget for two people:</B> 1100<BR><B>Zomato user rating:</B> 4.0<BR><BR><BR><B>Restaurant Name:</B> Jade Garden<BR><B>Restaurant locality address:</B> 123/27A, MG Marg, Civil Lines, Allahabad<BR><B>Average budget for two people:</B> 800<BR><B>Zomato user rating:</B> 4.0<BR><BR><BR><B>Restaurant Name:</B> Hotel Kanha Shyam<BR><B>Restaurant locality address:</B> Allahabad HO, Civil Lines, Allahabad<BR><B>Average budget for two people:</B> 900<BR><B>Zomato user rating:</B> 3.9<BR><BR><BR><B>Restaurant Name:</B> Moti Mahal Delux Tandoori Trail<BR><B>Restaurant locality address:</B> Shop 18A, Second Floor, Sardar Patel Marg, Above HDFC Bank, Civil Lines, Allahabad<BR><B>Average budget for two people:</B> 800<BR><B>Zomato user rating:</B> 3.8<BR><BR>==============================<BR>Bon Appetit!<BR><BR>Regards,<BR>Team Foodie.<BR><i>(This is an automatically generated email. Please do not reply. For any support please contact <b>support@foodie.com)</b></i>"}
    - utter_ask_to_send_mail
* greet{"email_id": "iashfaq@outlook.com"}
    - slot{"email_id": "iashfaq@outlook.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -8286763948484478505
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validatelocation
    - slot{"city_match": "notmatch"}
    - slot{"location": null}
    - utter_not_match_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validatelocation
    - slot{"city_match": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price_lowerlimit": "300"}
    - slot{"price_lowerlimit": "300"}
    - action_restaurant
    - slot{"email_response": null}
    - slot{"price_lowerlimit": null}
    - slot{"price_upperlimit": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - utter_no_result_price
    - utter_goodbye
    - export