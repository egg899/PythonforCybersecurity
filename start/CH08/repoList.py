import requests
import json
from dotenv import load_dotenv
import os

# Cargar variables
load_dotenv()

# Obtener el token
token_github = os.getenv("GITHUB_TOKEN")


url = "https://api.github.com/user/repos"
payloads = {}
headers = {
    "Authorization": f"token {token_github}"
}

response = requests.get(url, headers=headers, data=payloads)

print(response.status_code)
print(response.json())