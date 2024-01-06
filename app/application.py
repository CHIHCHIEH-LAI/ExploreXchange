from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from app.auth.router import router as auth_router
from app.trip_service.router import router as trip_service_router
from app.config import MIDDLEWARE_SECRET_KEY, FRONTEND_TEMPLATE_DIR

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=MIDDLEWARE_SECRET_KEY)
app.include_router(auth_router)
app.include_router(trip_service_router)

templates = Jinja2Templates(directory=FRONTEND_TEMPLATE_DIR)

@app.get('/')
def public(request: Request):
    user = request.session.get('user')
    if user:
        name = user.get('name')
        return templates.TemplateResponse('home.html', {'request': request, 'name': name})
    return templates.TemplateResponse('login.html', {'request': request})