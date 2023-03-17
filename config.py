# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25401847"))
API_HASH = os.environ.get("API_HASH", "ca8a79df8704ed676fca6891b7bc08ce")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6098282634:AAEMPBFy2-xi9b9Er2lmlTzXnQhLYAI4RCo")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5989342270")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "urlshortnerbo")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://postbot:postbot@cluster0.ouwne8q.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5989342270")) 
ADMINS.append(5989342270) if OWNER_ID not in ADMINS else []
ADMINS.append(5989342270)

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001963546070")) 

# For Force Subscription
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MoneyCaselinkupdate")

# true if forward should be avoided
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "False")

# image when someone hit /start
WELCOME_IMAGE = os.environ.get("https://telegra.ph/file/81b13b6b326660dd49262.jpg", '')
LINK_BYPASS = "False"
