import logging
from utils import parse

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
    