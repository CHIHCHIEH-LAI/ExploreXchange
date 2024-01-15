from dotenv import load_dotenv
import os

load_dotenv()

BASE_URI = 'http://127.0.0.1:8000'
MIDDLEWARE_SECRET_KEY = os.getenv('MIDDLEWARE_SECRET_KEY')

PROJECT_DIR_PATH = os.getenv('PROJECT_DIR_PATH')
FRONTEND_TEMPLATE_DIR = 'app/frontend/templates'