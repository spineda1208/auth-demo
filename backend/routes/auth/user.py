from flask import Blueprint, request
from dataclasses import asdict
import json
import jwt

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/", methods=["GET"])
def GET():
    user_jwt = request.cookies.get("jwt")
    assert user_jwt is not None

    if not jwt:
        return json.dumps({"error": "No authentication token provided"}), 401

    if not jwt.verify(user_jwt):
        return json.dumps({"error": "Invalid authentication token"}), 401

    # Extract user_id from JWT and get user data
    user_info = get_authentication(jwt)
    user = db.select.user_by_id(user_info.user_id)

    return json.dumps(asdict(user)), 200
