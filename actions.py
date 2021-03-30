from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import requests
import asyncio
import re
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor

r_email_rest = []
from email.message import EmailMessage

import zomatopy
import json
import smtplib
from email.message import EmailMessage

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"d7d2afaf2f19d43708fb09bbe480d6b0"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
	
		global response
		global cnt
		
		#find budget boundary
		minBudget, maxBudget = getMinMaxBudget(price);
		location_detail=zomato.get_location(loc, 1)
		
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5, 'american':1, 'mexican':73, 'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		
		json_results = json.loads(results)
		
		#filter by budget
		temp_dict={}
		final_dict={}

		cnt = json_results['results_found']

		if json_results['results_found'] == 0:
			response= "no results"
		else:
			i=0
			for restaurant in json_results['restaurants']:
				temp_dict=[restaurant['restaurant']["user_rating"]["aggregate_rating"],restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'], restaurant['restaurant']['average_cost_for_two']]
				if (temp_dict[3] >= minBudget) and (temp_dict[3] <= maxBudget):						
					final_dict[i] = temp_dict
					i=i+1
		
		#sort by rating
		sorted_dict={}
		for k, v in sorted(final_dict.items(), key=lambda item: item[1][0], reverse=True):
			sorted_dict[k]=v
		
		#prepare top 5 response
		response=""
		if len(sorted_dict) == 0:
			response= "no results"
		else:
			i=0;
			for k, v in sorted_dict.items():
				i=i+1
				response=response+ "Found "+ v[1]+ " in "+ v[2]+ " where price for two people is Rs." +str(v[3]) +" and rating is " +str(v[0])+"..."+"\n"
				if (i == 5):
					break;
		
		dispatcher.utter_message("-----"+response)
		
		return [SlotSet('location',loc)]
		

class ActionSendEmail(Action):
    #Define action name
    def name(self):
        return 'action_send_email'
        

    def run(self, dispatcher, tracker, domain):
        #Get user's email id
        to_email = tracker.get_slot('email')

        #Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global response
        email_rest_count = len(r_email_rest)
        #Construct the email 'subject' and the contents.
        r_email_subj = "Top " + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        r_email_msg = "Hello this is your personal Foodie assistant. As per your requirements, here are the " + r_email_subj + "." + "\n" + "\n" +"\n"
        rest_num = 0
        for restaurant in r_email_rest:
            rest_num +=1
            r_email_msg = r_email_msg + "Restaurant " + str(rest_num) +": " + str(restaurant['restaurant']['name'])+ " in " + str(restaurant['restaurant']['location']['address']) + " has been rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + ".The average budget for 2 people is: " + str(restaurant['restaurant']['average_cost_for_two']) + "\n" + "\n"

        #Open SMTP connection to Foodie's email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("foodie.bot.donotreply@gmail.com", "foodiebot12345")

        #Create the msg object
        msg = EmailMessage()

        #Fill in the message properties
        msg['Subject'] = r_email_subj
        msg['From'] = "foodie.bot.donotreply@gmail.com"

        #Fill in the message content
        msg.set_content(response)
        msg['To'] = to_email
        
        #Sent the message. If error catch and throw it
        try:
            s.send_message(msg)
            s.quit()
            dispatcher.utter_message("Email Sent. Please check your inbox. Have a great time!!")
        except (RuntimeError, TypeError, NameError, AttributeError):
            dispatcher.utter_message("Email server not responding at time")
        return []

def getMinMaxBudget(price):
    minBudget = 0
    maxBudget = 5000;
    
    if price == 'Lesser than Rs. 300':
        maxBudget = 300
    elif price == 'Rs. 300 to 700':
        minBudget = 300
        maxBudget = 700
    else:
        minBudget = 700
    return [minBudget, maxBudget]

class VerifyLocation(Action):
    #Define action
    def name(self):
        return "action_verify_location"
    
    def run(self, dispatcher, tracker, domain): 
        #Extract the list of tier 1 and 2 cities from wikipage
        url="https://en.wikipedia.org/wiki/Classification_of_Indian_cities"
        r = requests.get(url,verify=False)
        soup = BeautifulSoup(r.text, "html.parser")
    
        #Parse the content to extract names
        cities=list(map(lambda x:x.text.lower(),soup.find('table',class_='wikitable').find_all('a')))
        
        #Get the list of common synonym names for the cities in tier 1 and 2
        city_synonym=[]
        #Extract the common city synonyms from this page
        r=requests.get('https://www.scoopwhoop.com/news/whats-in-a-name/#.45rdcz1m2',verify=False)
        synonym_list=BeautifulSoup(r.text,'html.parser').find('div',class_='article-body').find_all('h2')
        
        #extract Synonym list
        for city in synonym_list:
            if re.search(r'^[0-9]{1,2}.+',city.text.strip()):
                city_synonym.append(city.text.strip().split()[1].lower())
                city_synonym.append(city.text.strip().split()[-1].lower())        
        
        #Few other city synonyms as gathered from the internet
        city_synonym_2 = ['allahabad','atal-nagar','bangalore','baroda','bejawada ','belagavi ','belgaum','benares','bengaluru',
                        'bijapur','bombay','calcutta ','calicut','cannanore','cawnpore ','chennai','cochin','gauhati',
                        'gulbarga ','gurgaon','gurugram ','guwahati ','hubballi ','hubli ','indhur','indore','jabalpur ',
                        'jajesmow ','jajmau','jubbulpore ','kalaburagi ','kannur','kanpur','kochi ','kolkata','kollam',
                        'kozhikode','kudanthai','kumbakonam ','madras','mangalore','mangaluru','mumbai','bombay','mysore','mysore',
                        'mysuru','nellore','panaji','panjim','pondicherry','poona ','prayagraj','puducherry ','pune',
                        'quilon','raipur','shimla','simhapuri','simla ','thiruvananthapuram','thrissur ','tindivanam ',
                        'tinnevelly ','tinthirivanam ','tiruchirapalli','tirunelveli','tiruvallikeni ','trichinopoly',
                        'trichur','triplicane ','trivandrum ','vadodara ','varanasi ','vatakara ','vijayapura ','vijayawada ',
                        'visakhapatnam ','waltair']
        
        #List of all valid cities in India for verification. Parse from this page
        url1="https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
        r1 = requests.get(url1,verify=False)
        soup1 = BeautifulSoup(r1.text, "html.parser")
        
        #Extract list of all cities in India
        all_cities_list = []
        temp_city=list(map(lambda x:x.text.lower(),soup1.find('table',class_='wikitable').find_all('a')))
        for city in temp_city:
            if not re.search(r'^.[0-9]{1,2}.+',city):
                all_cities_list.append(city)

        #get the location from user slot
        loc=tracker.get_slot('location')
        
        #Check for pincodes. Not supported for now
        if (loc.lower().isdigit()):
            dispatcher.utter_message("Sorry I am naive I dont understand pincodes and digits for now. Please try some actual place!!")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        #Check for invalid city
        elif not (loc.lower() in all_cities_list  or loc.lower() in city_synonym or loc.lower() in city_synonym_2 or loc.lower() in cities):
            dispatcher.utter_message("Sorry did'nt find any such location " + loc + " Can you please tell again?")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        #Check for valid city but no servicable by Zomato
        elif not (loc.lower() in city_synonym or loc.lower() in city_synonym_2 or loc.lower() in cities):
            dispatcher.utter_message("We do not operate in " + loc + " yet. Please try some other city.")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        #If valid city and servicable return true
        else:
            return [SlotSet('location',loc),SlotSet('location_ok',True)]

