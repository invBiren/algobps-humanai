class MSTOCK_SESSION:
    api_key = None
    jwt = None
    feed = None

    @classmethod
    def set(cls, api_key, jwt, feed):
        cls.api_key = api_key
        cls.jwt = jwt
        cls.feed = feed

    @classmethod
    def is_active(cls):
        return cls.jwt is not None
