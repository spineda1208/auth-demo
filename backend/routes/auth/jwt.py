import json
import hmac
import hashlib
import base64
from datetime import datetime, timedelta
import os
from typing import Optional


def new(user_id: int, client_id: int) -> str:
    # Create header
    header = {"alg": "HS256", "typ": "JWT"}
    header_encoded = (
        base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
    )

    # Create payload
    now = datetime.now()
    payload = {
        "user_id": user_id,
        "client_id": client_id,
        "iat": now.isoformat(),
        "exp": (now + timedelta(hours=9)).isoformat(),
    }
    payload_encoded = (
        base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
    )

    # Create signature
    secret = os.getenv("JWT_SECRET_KEY")
    if not secret:
        raise ValueError("JWT_SECRET_KEY environment variable is not set")

    prefix = f"{header_encoded}.{payload_encoded}"
    signature = hmac.new(secret.encode(), prefix.encode(), hashlib.sha256).digest()
    signature_encoded = base64.urlsafe_b64encode(signature).decode().rstrip("=")

    return f"{prefix}.{signature_encoded}"


def verify(jwt: str) -> bool:
    parts = jwt.split(".")
    if len(parts) != 3:
        return False

    base64_header, base64_payload, received_signature = parts

    secret = os.getenv("JWT_SECRET_KEY")
    if not secret:
        raise ValueError("JWT_SECRET_KEY environment variable is not set")

    prefix = f"{base64_header}.{base64_payload}"
    expected_signature = hmac.new(
        secret.encode(), prefix.encode(), hashlib.sha256
    ).digest()
    expected_signature_encoded = (
        base64.urlsafe_b64encode(expected_signature).decode().rstrip("=")
    )

    return hmac.compare_digest(expected_signature_encoded, received_signature)


def get_authentication(jwt: str) -> Optional[int]:
    # Verify token first
    if not verify(jwt):
        return None

    try:
        # Split JWT and get payload
        _, payload_b64, _ = jwt.split(".")

        # Decode payload
        payload_b64 += "=" * (-len(payload_b64) % 4)
        payload_json = base64.urlsafe_b64decode(payload_b64).decode("utf-8")
        payload = json.loads(payload_json)

        return payload["user_id"]

    except Exception:
        return None
