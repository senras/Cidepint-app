from authlib.integrations.flask_client import OAuth

o_auth = OAuth()

def init_oauth(app):
    CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
    o_auth.init_app(app)
    o_auth.register(
        name="google",
        client_id='829585066803-ic9cjd8fpdn6i1dhu1blpor4vm611rg0.apps.googleusercontent.com',
        client_secret='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',
        server_metadata_url=CONF_URL,
        client_kwargs={
            "scope": "openid email profile",
        }
    )
    return o_auth