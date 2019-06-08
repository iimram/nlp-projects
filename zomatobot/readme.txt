Restaurant search chatbot application that leverages both rasa nlu and rasa core modules of the rasa NLP framework.
Used zomato api for restaurant search based on city, cuisine and price range.
Run nul_model.py file to train the rasa nlu model that extracts entities and identifies intents.
Run the dialog_management_model.py file to train the dialog flow/rasa core and launch the chatbot in command line.
Run the train_online.py file to trainin rasa core and interactively add new stories to stories.md file.
Update data.json file to add more data for entity extraction and intent recognition.
actions.py file has the code for all actions like restaurant_search, etc.
