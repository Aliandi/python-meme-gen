import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    USER = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
