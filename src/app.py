from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return f"It works! {name}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')