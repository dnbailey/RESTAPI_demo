from flask import Flask, jsonify
import csv

def find_name(name):
    with open("data.csv", newline="") as file:
        data = csv.DictReader(file)
        for line in data:
            if name.lower() == line['fname'].lower():
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
def get_user(user_name):
    user_data = find_name(user_name)
    if user_data == "Not found":
        return "Not found", 404
    
    return jsonify({"firstName": user_data['fname'], "last_name": user_data['lname']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')