from flask import Blueprint, request
import password
import hmac
import hashlib
import db

login = Blueprint("login", __name__, url_prefix="/login")


@login.route("/", methods=["POST"])
def POST():
    json = request.get_json()

    email = json["email"]
    pswrd = json["password"]

    hashed_password = db.select.user_password(email)
    if not password.verify(pswrd, hashed_password):
        return json.dumps({"error": "incorrect password"}), 400

    user_id = db.select.user_id(email)
    client_id = request.remote_addr
    jwt = new_token(user_id, client_id)

    # Create response with cookie
    response = make_response({"message": "Login successful"})
    response.set_cookie("jwt", jwt, httponly=True, secure=True, samesite="Strict")

    return response
