from fastapi import FastAPI
from app.service.router import router as service_router

app = FastAPI()

app.include_router(service_router)
