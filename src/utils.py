from flask import request, abort
import csv

def parse(filename):
    with open(filename, newline="") as file:
        data = csv.DictReader(file)
        return list(data)


def require_apikey(route_function):
    def decorated_function(*args, **kwargs):
        headers = request.headers
        if headers.get("X-Api-Key") and headers.get("X-Api-Key") == "123":
            return route_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

if __name__ == "__main__":
    print("This should not be ran standalone.")
