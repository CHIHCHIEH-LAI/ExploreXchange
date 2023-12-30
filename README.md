# ExploreXchange

## Tech Stack
- Python
- FastAPI
- Google OAuth2
- SQLModel

## PostgreSQL Database Engine
1. ```docker pull postgres```
2. ```docker run --name exploreXchange_db -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -d postgres```
3. ```psql -h localhost -p 5432 -d postgres -U postgres```

## Material Link
- OAuth: https://docs.authlib.org/en/latest/client/fastapi.html
- PostgreSQL: https://github.com/CHIHCHIEH-LAI/Elixir_Payroll_API#setting-up-postgresql
- SQLModel: https://sqlmodel.tiangolo.com/tutorial/many-to-many/
