from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

from app.auth.config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_SERVER_META_URL

class google_oauth:
    def __init__(self) -> None:
        config_data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}
        starlette_config = Config(environ=config_data)
        oauth = OAuth(starlette_config)
        oauth.register(
            name='google',
            server_metadata_url=GOOGLE_SERVER_META_URL,
            client_kwargs={'scope': 'openid email profile'},
        )