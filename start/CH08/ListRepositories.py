#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By Alberto German Verissimo on April 26, 2022


##Let's get the authorization of the API
# import requests

# url = "https://api.github.com/user/repos"

# payload={}
# headers = {
#   'Authorization': 'token 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'
# }

# # response = requests.request("GET", url, headers=headers, data=payload)

# # print(response.text)


# #Let's turn this response into a json object 
# import json

# def get_user():
#     response = requests.request("GET", url, headers=headers, data=payload)
#     # request_uri =response.text
#     # r = requests.get(request_uri)
#     items=response.json()
#     return items

# user = get_user()

# for i in range(len(user)):
    
#     print(user[i]['id'])

# # print(json.dumps(user, indent=2))


import requests
import configparser

def get_api_key(key_name):
  #Create configparser object and load file
  config = configparser.ConfigParser()
  config.read("/Users/user/Desktop/Programming and data analysis/Udemy/Cybersecurity/secrets.ini")
  #Get the Api Key and return
  api_key = config["APIkeys"][key_name]
  return api_key

#Get API key from file
token = get_api_key('Github')

url = "https://api.github.com/user/repos"

payload={}
headers = {
  'Authorization': 'token ' + token
}


# response = requests.request("GET", url, headers=headers, data =payload)

# print(response.text)

# #Let's turn this response into a json object 
# import json

def get_user():
    response = requests.request("GET", url, headers=headers, data=payload)
    # request_uri =response.text
    # r = requests.get(request_uri)
    items=response.json()
    return items


user = get_user()
# print(user[0].keys())
for i in range(len(user)):
  print(user[i]['id'],'\n', user[i]['full_name'],'\n', user[i]['hooks_url'],'\n', user[i]['comments_url'],'\n','\n')
  
 