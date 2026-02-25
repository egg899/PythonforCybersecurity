#!/usr/bin/env python3
# Script that tells us how many people there are in space
#By Alberto German Verissimo on April 25, 2022

#Import Python mdules
import requests
import json

# def get_people_in_space():
#     request_uri = "http://api.open-notify.org/astros.json"
#     r = requests.get(request_uri)
#     items = r.json()
#     return items

## Example of the function with a BEARER
def get_people_in_space():
    request_uri = "http://api.open-notify.org/astros.json"

    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4N2RkZTlkOTc4MTljMzBmOTFhMTJkYiIsImlhdCI6MTc2NjA5NTA4NywiZXhwIjoxNzY2Njk5ODg3fQ.Xy1XrN_gcR3HUDxTSjr1O9e2l50jos8QRCB-cAroVDc",
        "Content-Type":"application/json"
    }

    r = requests.get(request_uri, headers=headers)
    items = r.json()
    return items 


astronauts = get_people_in_space()

# print basic details    
print(astronauts)    

#print "pretty" json
print(json.dumps(astronauts, indent=2))

#search through datad to return specific information
print("There are {0} people in space right now". format(astronauts["number"]))
print("The first astronauts is {0} aboard the {1}".format(astronauts["people"][0]["name"], astronauts["people"][0]["craft"]))


#Loop through all the people
print("Full list of people in space")
for person in astronauts["people"]:
    print("{0} is aboard the {1}".format(person["name"], person["craft"]))

