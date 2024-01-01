from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

class GoogleOAuthManager:
    def __init__(self, client_id: str, client_secret: str, server_metadata_url: str) -> None:
        self.google_client_id = client_id
        self.google_client_secret = client_secret
        self.google_server_meta_url = server_metadata_url

        if not all([self.google_client_id, self.google_client_secret, self.google_server_meta_url]):
            raise ValueError("Google OAuth environment variables are not set properly.")

        self.oauth = self.configure_oauth()

    def configure_oauth(self) -> OAuth:
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

    def get_oauth(self) -> OAuth:
        return self.oauth