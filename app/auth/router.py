from authlib.integrations.starlette_client import OAuthError
from fastapi import APIRouter
from fastapi import Request
from starlette.responses import RedirectResponse

from app.auth.oauth import GoogleOAuth

router = APIRouter()

googleOAuth = GoogleOAuth()
oauth = googleOAuth.get_oauth()

@router.route('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.route('/auth')
async def auth(request: Request):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return RedirectResponse(url='/')
    user_data = access_token.get('userinfo')
    print(dict(user_data))
    if user_data:
        request.session['user'] = dict(user_data)
    return RedirectResponse(url='/')

@router.route('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')