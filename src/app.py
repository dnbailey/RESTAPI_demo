from flask import Flask, jsonify, request
from utils import parse, require_apikey
import logging

logging.basicConfig(filename="app.log", filemode="w",
                    format="%(name)s - %(levelname)s - %(message)s")

data = parse("data.csv")


def find_person(name, type):
    if type != "f" and type != 'l':
        logging.info("User did not specify f or l")
    else:
        for line in data:
            if name.lower() == line[type + 'name'].lower():
                return line
    return "Not found"


def find_state(state):
    for line in data:
        if state.lower() == line['state'].lower():
            return line
    return "Not found"


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"response": "It works!"})


@app.route('/user/')
def user():
    return jsonify("No user defined."), 404


@app.route('/user/<user_name>')
@require_apikey
def get_user(user_name):
    f_or_l = request.args.get("type")
    user_data = find_person(user_name, f_or_l)
    if user_data == "Not found":
        return jsonify(f"{user_name} not found"), 404

    return jsonify({"firstName": user_data['fname'], "last_name": user_data['lname']})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
