from authlib.integrations.starlette_client import OAuthError
from fastapi import APIRouter, Request, Depends
from starlette.responses import RedirectResponse

from app.auth.dependencies import get_google_oauth

router = APIRouter()

@router.route('/login')
async def login(
    request: Request,
    oauth = Depends(get_google_oauth)
):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.route('/auth')
async def auth(
    request: Request,
    oauth = Depends(get_google_oauth)
):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return RedirectResponse(url='/')
    user_data = access_token.get('userinfo')
    if user_data:
        request.session['user'] = dict(user_data)
    return RedirectResponse(url='/')

@router.route('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')