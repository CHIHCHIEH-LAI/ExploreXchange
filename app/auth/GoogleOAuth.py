from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

from app.auth.config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_SERVER_META_URL

class GoogleOAuth:
    def __init__(self):
        self.google_client_id = GOOGLE_CLIENT_ID
        self.google_client_secret = GOOGLE_CLIENT_SECRET
        self.google_server_meta_url = GOOGLE_SERVER_META_URL

        if not all([self.google_client_id, self.google_client_secret, self.google_server_meta_url]):
            raise ValueError("Google OAuth environment variables are not set properly.")

        self.oauth = self.configure_oauth()

    def configure_oauth(self):
        config_data = {
            'GOOGLE_CLIENT_ID': self.google_client_id,
            'GOOGLE_CLIENT_SECRET': self.google_client_secret
        }
        starlette_config = Config(environ=config_data)
        oauth = OAuth(starlette_config)
        oauth.register(
            name='google',
            server_metadata_url=self.google_server_meta_url,
            client_kwargs={'scope': 'openid email profile'},
        )
        return oauth

    def get_oauth(self):
        return self.oauth