import sys
import json

AuthFile="../Logins.encrypted.json"

email = sys.argv[1].lower()

with open(AuthFile, "r") as f:
    data = json.load(f)
    for user in data:
        if data[user]["email"].lower() == email:
            print(data[user]["username"])
            break