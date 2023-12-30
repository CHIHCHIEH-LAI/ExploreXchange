from fastapi import APIRouter

from app.database.config import DATABASE_URI
from app.database.DatabaseManager import DatabaseManager

router = APIRouter()

databaseManager = DatabaseManager(DATABASE_URI)

@router.route('/db/create_tables')
async def create_tables():
    databaseManager.create_all_tables()

@router.route('/db/delete_tables')
async def delete_tables():
    databaseManager.delete_all_tables()

