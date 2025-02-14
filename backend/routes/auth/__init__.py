from flask import Blueprint
from .login import login
from .signup import signup
from .user import user

auth = Blueprint("auth", __name__, url_prefix="/auth")
auth.register_blueprint(signup)
auth.register_blueprint(login)
auth.register_blueprint(user)
