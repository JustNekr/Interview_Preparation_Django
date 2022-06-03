from .base import *
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True


SITE_ID = 1
