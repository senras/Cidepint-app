from authlib.integrations.flask_client import OAuth

o_auth = OAuth()

def init_oauth(app):
    CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
    o_auth.init_app(app)
    o_auth.register(
        name="google",
        client_id='1030370667179-rgj6g8s39f1pq0u22ksoqsbsv9v1spiv.apps.googleusercontent.com',
        client_secret='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',
        server_metadata_url=CONF_URL,
        client_kwargs={
            "scope": "openid email profile",
        }
    )
    return o_auth