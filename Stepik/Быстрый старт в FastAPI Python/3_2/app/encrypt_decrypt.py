from itsdangerous import URLSafeTimedSerializer

token_serializer = URLSafeTimedSerializer(secret_key="shifr")


def encrypt_decrypt(uuid_time, ecrypt: bool = True):
    if ecrypt:
        return token_serializer.dumps(uuid_time)
    else:
        return token_serializer.loads(uuid_time)
