import json
import os

FILE = "database/users.json"

def load_user():

    if os.path.exists(FILE):

        with open(FILE, "r", encoding="utf-8") as f:

            try:
                return json.load(f)

            except:

                return {}

    return {}

def save_user(data):

    with open(FILE, "w", encoding="utf-8") as f:

        json.dump(data, f, indent=4)
