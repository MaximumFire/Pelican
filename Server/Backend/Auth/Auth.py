import sys
import hashlib
import json

AuthFile="../../Logins.encrypted.json"


email=sys.argv[1] #Requested email, for blank ""
password=hashlib.sha256(sys.argv[2].encode()).hexdigest() #Requested password, for blank ""

with open(AuthFile, "r") as f:
    Logins = json.load(f)
    for login in Logins:
        accpassword = Logins[login]["password"]
        accemail = Logins[login]["email"]
        if accemail.lower() == email.lower() and accpassword == password:
            print("Login Success")
            exit()
print("Login Failed")
