import configparser
import os
from dotenv import load_dotenv


# Cargar variables
load_dotenv()

# Obtener el token
token_github = os.getenv("GITHUB_TOKEN")

config = configparser.ConfigParser()
config["APIkeys"] = { "GitHub": token_github }

#Save the file in same directory as the script
#file_path = os.path.join(os.path.dirname(__file__), "secret.ini")
file_path = os.path.join(os.path.dirname(__file__), "../../..","secret.ini")



with open(file_path, "w") as configfile:
    config.write(configfile)

print(f"File saved to: {file_path}")