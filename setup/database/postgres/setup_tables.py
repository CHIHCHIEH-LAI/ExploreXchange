from setup.database.postgres.config import DATABASE_URI
from setup.database.postgres.postgres_tables import postgres_tables

tables = postgres_tables(DATABASE_URI)
tables.recreate()