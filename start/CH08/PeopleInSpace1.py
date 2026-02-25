# paste code here

# import requests

# url = "http://api.open-notify.org/astros.json"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)



import requests

url = "http://api.open-notify.org/astros.json"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4N2RkZTlkOTc4MTljMzBmOTFhMTJkYiIsImlhdCI6MTc2NjA5NTA4NywiZXhwIjoxNzY2Njk5ODg3fQ.Xy1XrN_gcR3HUDxTSjr1O9e2l50jos8QRCB-cAroVDc'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
