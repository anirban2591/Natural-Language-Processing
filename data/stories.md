
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye


## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye


## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye





## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye


## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_verify_location
    - slot{"location": "Jaipur"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye


## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"location": "gandhinagar"}
    - slot{"location": "gandhinagar"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_verify_location
    - slot{"location": "kochi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "kochi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye


## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"location": "gandhinagar"}
    - slot{"location": "gandhinagar"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_verify_location
    - slot{"location": "kochi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "kochi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye


## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"location": "gandhinagar"}
    - slot{"location": "gandhinagar"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "kochi"}
    - action_verify_location
    - slot{"location": "kochi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "kochi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye



## interactive_story_11
* restaurant_search{"cuisine": "mexican", "location": "mysore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mysore"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email_response
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_12
* restaurant_search{"cuisine": "american", "location": "surat"}
    - slot{"cuisine": "american"}
    - slot{"location": "surat"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_13
* restaurant_search{"cuisine": "italian", "location": "jablpur", "email": "anirban2591@gmail.com"}
    - slot{"cuisine": "italian"}
    - slot{"email": "anirban2591@gmail.com"}
    - slot{"location": "jablpur"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "jablpur"}
    - action_send_email
    - utter_goodbye


## interactive_story_14
* restaurant_search{"location": "puducherry"}
    - slot{"location": "puducherry"}
    - action_verify_location
    - slot{"location": "puducherry"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "puducherry"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_15
* restaurant_search{"location": "naharlagun"}
    - slot{"location": "naharlagun"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye



## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye
## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

* goodbye
    - utter_goodbye


## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "jabalpur"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "jabalpur"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "ajmer"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "agra"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "poonammadan2020@gmail.com"}
    - slot{"email": "poonammadan2020@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gorakhpur"}
    - slot{"location": "gorakhpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "gorakhpur"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ghaziabad"}
    - slot{"location": "ghaziabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "ghaziabad"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "gurgaon"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "indore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "indore"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "poonammadan2020@gmail.com"}
    - slot{"email": "poonammadan2020@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_ask_location
* restaurant_search{"location": "gwalior"}
    - slot{"location": "gwalior"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "gwalior"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "kapilmaan92@gmail.com"}
    - slot{"email": "kapilmaan92@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "indian", "location": "bombay", "price": "<300"}
    - slot{"cuisine": "indian"}
    - slot{"location": "bombay"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - slot{"location": "bombay"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "madan_64@rediffmail.com"}
    - slot{"email": "madan_64@rediffmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* affirm{"location": "guwahati"}
    - slot{"location": "guwahati"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "guwahati"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "banglore"}
    - slot{"location": "banglore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - utter_ask_price
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "banglore"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "gurgaon"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_nonoperable_location

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"location": "kundam"}
    - slot{"location": "kundam"}
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "singrauli"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "singrauli"}
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"location": "ramgarh"}
    - slot{"location": "ramgarh"}
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"location": "chhindwara"}
    - slot{"location": "chhindwara"}
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search
    - utter_nonoperable_location

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "nagpur"}
    - utter_ask_email_response
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "jabalpur", "price": "300-700", "email": "anirban2591@gmail.com"}
    - slot{"cuisine": "italian"}
    - slot{"email": "anirban2591@gmail.com"}
    - slot{"location": "jabalpur"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "jabalpur"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "mumbai", "email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - utter_ask_price
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian", "email": "anirban2591@gmail.com"}
    - slot{"cuisine": "italian"}
    - slot{"email": "anirban2591@gmail.com"}
    - utter_ask_location
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - utter_ask_price
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "email": "anirban2591@gmail.com"}
    - slot{"cuisine": "chinese"}
    - slot{"email": "anirban2591@gmail.com"}
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"location": "banglore", "email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - slot{"location": "banglore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "banglore"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "sangli"}
    - slot{"location": "sangli"}
    - utter_nonoperable_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "sydney"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "sydney"}
    - utter_nonoperable_location
* restaurant_search{"location": "new york"}
    - slot{"location": "new york"}
    - utter_nonoperable_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye


## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "udaipur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "udaipur"}
    - utter_nonoperable_location
* restaurant_search{"location": "gangapur"}
    - slot{"location": "gangapur"}
    - utter_nonoperable_location
* restaurant_search
    - utter_nonoperable_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - utter_nonoperable_location
* restaurant_search{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "nagpur"}
    - utter_ask_email_response
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_nonoperable_location
* restaurant_search{"location": "bhilai"}
    - slot{"location": "bhilai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": ">300"}
    - slot{"price": ">300"}
    - action_search_restaurants
    - slot{"location": "bhilai"}
    - utter_ask_email_response
* email_response{"email_response": "no"}
    - slot{"email_response": "no"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "jaipur"}
    - slot{"cuisine": "american"}
    - slot{"location": "jaipur"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "jaipur"}
    - utter_ask_email_response
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "jabalpur"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "nagpur"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "bhilai"}
    - slot{"cuisine": "american"}
    - slot{"location": "bhilai"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "bhilai"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "sagar"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "sagar"}
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "indore", "price": "300-700"}
    - slot{"cuisine": "american"}
    - slot{"location": "indore"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"price": ">300"}
    - slot{"price": ">300"}
    - utter_ask_location
* restaurant_search{"location": "sagar"}
    - slot{"location": "sagar"}
    - utter_nonoperable_location
* restaurant_search{"location": "jabaplur"}
    - slot{"location": "jabaplur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"location": "jabaplur"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "bhilai"}
    - slot{"location": "bhilai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "bhilai"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - utter_ask_location
* restaurant_search{"location": "amravati"}
    - slot{"location": "amravati"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "amravati"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - utter_ask_location
* affirm{"location": "goa"}
    - slot{"location": "goa"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"location": "goa"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_ask_location
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "goa"}
    - slot{"cuisine": "italian"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "goa"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "vellore"}
    - slot{"cuisine": "american"}
    - slot{"location": "vellore"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "vellore"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "indian", "price": "300-700"}
    - slot{"cuisine": "indian"}
    - slot{"price": "300-700"}
    - utter_ask_location
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
    - action_search_restaurants
    - slot{"location": "warangal"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "price": ">300"}
    - slot{"cuisine": "chinese"}
    - slot{"price": ">300"}
    - utter_ask_location
* restaurant_search{"location": "meerut"}
    - slot{"location": "meerut"}
    - action_search_restaurants
    - slot{"location": "meerut"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "firozabad", "price": ">300"}
    - slot{"location": "firozabad"}
    - slot{"price": ">300"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "firozabad"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "Varanasi", "price": ">700"}
    - slot{"location": "Varanasi"}
    - slot{"price": ">700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Varanasi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "reva"}
    - slot{"location": "reva"}
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "seoni"}
    - slot{"cuisine": "italian"}
    - slot{"location": "seoni"}
    - utter_nonoperable_location

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "mysore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mysore"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email_response
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "surat"}
    - slot{"cuisine": "american"}
    - slot{"location": "surat"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "jablpur", "email": "anirban2591@gmail.com"}
    - slot{"cuisine": "italian"}
    - slot{"email": "anirban2591@gmail.com"}
    - slot{"location": "jablpur"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "jablpur"}
    - action_send_email
    - utter_goodbye


## interactive_story_1
* restaurant_search{"location": "puducherry"}
    - slot{"location": "puducherry"}
    - action_verify_location
    - slot{"location": "puducherry"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "puducherry"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "naharlagun"}
    - slot{"location": "naharlagun"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email_response
* email_response{"email_response": "No"}
    - slot{"email_response": "No"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "calcutta"}
    - slot{"cuisine": "american"}
    - slot{"location": "calcutta"}
    - action_verify_location
    - slot{"location": "calcutta"}
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "calcutta"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "kolkata"}
    - slot{"cuisine": "american"}
    - slot{"location": "kolkata"}
    - action_verify_location
    - slot{"location": "kolkata"}
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_response
* email_response{"email_response": "Yes"}
    - slot{"email_response": "Yes"}
    - utter_ask_email
* email{"email": "anirban2591@gmail.com"}
    - slot{"email": "anirban2591@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye




