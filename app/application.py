from fastapi import FastAPI
from fastapi import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse

from app.auth.router import router as auth_router
from app.trip_service.router import router as trip_service_router
from app.config import MIDDLEWARE_SECRET_KEY

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=MIDDLEWARE_SECRET_KEY)

app.include_router(auth_router)
app.include_router(trip_service_router)

@app.get('/')
def public(request: Request):
    user = request.session.get('user')
    if user:
        name = user.get('name')
        return HTMLResponse(f'<p>Hello {name}!</p><a href=/logout>Logout</a>')
    return HTMLResponse('<a href=/login>Login</a>')

# from app.models.event import Event
# from datetime import datetime
# from app.database.mongo.config import MONGODB_URI, DATABASE
# from app.database.mongo.database_manager import DatabaseManager
# from app.database.mongo.trip_collection_manager import TripCollectionManager

# dbMgr = DatabaseManager(MONGODB_URI, DATABASE)
# colMgr = TripCollectionManager(dbMgr, 'trips')

# trip = Trip(
#     title="Mountain Adventure",
#     start_time=datetime(2023, 1, 1, 9, 0),
#     end_time=datetime(2023, 1, 4, 10, 0),
#     location="Mountains",
#     description="A trip to the mountains",
#     owner="Alice",
#     events=[
#         Event(
#             title="Hiking",
#             start_time=datetime(2023, 1, 1, 10, 0),
#             end_time=datetime(2023, 1, 1, 12, 0),
#             description="A trip to the mountains",
#             owner="Alice"
#         ),
#         Event(
#             title="Camping",
#             start_time=datetime(2023, 1, 2, 15, 0),
#             end_time=datetime(2023, 1, 3, 10, 0),
#             location="Campground",
#             owner="Alice"
#         )
#     ]
# )

# colMgr.create_trip(trip)
# docs = colMgr.query_all_trips_of_owner('Alice')
# print(docs)
# doc = colMgr.query_trip_by_id('65915d3abd6eb1e6ae071420')
# trip = Trip(**doc)
# print(trip)
# colMgr.delete_trip_by_id('65915d3abd6eb1e6ae071420')
# colMgr.clean_collection('trips')