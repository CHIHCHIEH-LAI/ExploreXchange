from app.auth.google_oauth_manager import GoogleOAuthManager
from app.auth.config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_SERVER_META_URL

def get_google_oauth():
    googleOAuth = GoogleOAuthManager(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_SERVER_META_URL)
    return googleOAuth.get_oauth()