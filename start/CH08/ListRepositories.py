#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By Alberto German Verissimo on April 26, 2022


##Let's get the authorization of the API
import requests

url = "https://api.github.com/user/repos"

payload={}
headers = {
  'Authorization': 'token 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'
}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)


#Let's turn this response into a json object 
import json

def get_user():
    response = requests.request("GET", url, headers=headers, data=payload)
    # request_uri =response.text
    # r = requests.get(request_uri)
    items=response.json()
    return items

user = get_user()

for i in range(len(user)):
    
    print(user[i]['id'])

# print(json.dumps(user, indent=2))