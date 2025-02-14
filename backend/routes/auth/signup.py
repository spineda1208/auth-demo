from flask import Blueprint, request
from db.types import User
import password
import db
import hashlib
import hmac

signup = Blueprint("signup", __name__, url_prefix="/signup")


@signup.route("/", methods=["POST"])
def POST():
    json = request.get_json()

    email = json["email"]
    pswrd = json["password"]
    first_name = json["first_name"]
    last_name = json["last_name"]
    ssn = json["ssn"]

    if any(
        x is None
        for x in [
            email,
            password,
            first_name,
            last_name,
            ssn,
        ]
    ):
        return json.dumps({"error": "incomplete form"}), 400

    hashed_password = password.hash(pswrd)
    user_id = db.insert.user(
        User(None, email, hashed_password, first_name, last_name, ssn)
    )

    return "", 200
