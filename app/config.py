from dotenv import load_dotenv
import os

load_dotenv()

BASE_URI = 'http://127.0.0.1:8000'
MIDDLEWARE_SECRET_KEY = os.getenv('MIDDLEWARE_SECRET_KEY')