from itsdangerous import URLSafeTimedSerializer

token_serializer = URLSafeTimedSerializer(secret_key="shifr")


def encrypt_decrypt(uuid, ecrypt: bool = True):
    if ecrypt:
        return token_serializer.dumps(uuid)
    else:
        return token_serializer.loads(uuid)
