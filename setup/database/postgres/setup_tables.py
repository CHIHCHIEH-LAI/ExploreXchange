from setup.database.postgres.postgres_tables import postgres_tables
from setup.database.postgres.config import DATABASE_URI
from setup.database.postgres.schema import Base

tables = postgres_tables(DATABASE_URI, Base)

tables.initialize()