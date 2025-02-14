import hmac
import hashlib
from environment.variables import PASSWORD_SECRET_KEY


def hash(password: str) -> str:
    hashed_password = hmac.new(
        PASSWORD_SECRET_KEY.encode("utf-8"), password.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    return hashed_password


def verify(password: str, hashed_password: str) -> bool:
    new_hash = hmac.new(
        PASSWORD_SECRET_KEY.encode("utf-8"), password.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(new_hash, hashed_password)
