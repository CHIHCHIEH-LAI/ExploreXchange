from authlib.integrations.starlette_client import OAuthError
from fastapi import APIRouter
from fastapi import Request
from starlette.responses import RedirectResponse

router = APIRouter()

@router.route('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')  # This creates the url for our /auth endpoint
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.route('/auth')
async def auth(request: Request):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return RedirectResponse(url='/')
    user_data = await oauth.google.parse_id_token(request, access_token)
    request.session['user'] = dict(user_data)
    return RedirectResponse(url='/')

@router.route('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')