import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    USER = os.getenv('API_USERNAME')
    PASSWORD = os.getenv('API_PASSWORD')
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")