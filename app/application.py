from fastapi import FastAPI
from fastapi import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse

from app.auth.router import router as auth_router
from app.service.router import router as service_router
from app.config import MIDDLEWARE_SECRET_KEY

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=MIDDLEWARE_SECRET_KEY)

app.include_router(auth_router)
app.include_router(service_router)

@app.get('/')
def public(request: Request):
    user = request.session.get('user')
    if user:
        name = user.get('name')
        return HTMLResponse(f'<p>Hello {name}!</p><a href=/logout>Logout</a>')
    return HTMLResponse('<a href=/login>Login</a>')