from flask import jsonify, request
from search import *
from utils import *
from app import app

@app.route('/')
def index():
    return """
    <html>
    <head>
    <title>Flask REST API</title>
    </head>
    <body>
        <h1>Welcome to the Flask API Demo</h1>
        <p>Try requesting a user using &lt;url&gt;/user/&lt;user_name\&gt;?type=&lt;f or l&gt;</p>
    </body>
    </html>
    """


@app.route('/user/', defaults={"user_name": "none"})
@app.route('/user/<user_name>')
@require_apikey
def get_user(user_name):
    f_or_l = request.args.get("type")
    user_data = find_person(user_name, f_or_l)
    if user_data == "Not found":
        return jsonify(f"{user_name} not found"), 404

    return jsonify({"firstName": user_data['fname'], "last_name": user_data['lname']})
