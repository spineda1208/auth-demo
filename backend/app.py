from flask import Flask, request
from routes.api import api
import json

app = Flask(__name__)
app.register_blueprint(api)


@app.before_request
def check_content_type():
    if not request.is_json:
        return (
            json.dumps({"error": "invalid content-type. expected application/json"}),
            415,
        )


@app.route("/", methods=["POST"])
def echo():
    return json.dumps(request.get_json()), 200, {"Content-Type": "application/json"}


if __name__ == "__main__":
    app.run(debug=True)
