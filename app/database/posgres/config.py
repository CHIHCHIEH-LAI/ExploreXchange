from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DATABASE_PASSWORD = os.getenv('POSTGRES_DATABASE_PASSWORD')
DATABASE_URI = f'postgres+psycopg2://postgres:{POSTGRES_DATABASE_PASSWORD}@localhost:5432/postgres'