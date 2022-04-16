import sys, os
import hashlib
import json

AuthFile="../Logins.encrypted.json"


#--
def getSalt(email):
    with open(AuthFile, "r") as f:
        Logins = json.load(f)
        for login in Logins:
            if email.lower() == Logins[login]["email"]:
                salt = Logins[login]["salt"]
                AuthFile.close()
                return salt
        AuthFile.close()
        return False
#--


email=sys.argv[1] #Requested email, for blank ""
salt = getSalt(email)
if salt:
    password=hashlib.sha256(f"{sys.argv[2]}{salt}".encode()).hexdigest()
else:
    print("user not found")


with open(AuthFile, "r") as f:
    Logins = json.load(f)
    for login in Logins:
        accpassword = Logins[login]["password"]
        accemail = Logins[login]["email"]
        if accemail.lower() == email.lower() and accpassword == password:
            print("Login Success")
            exit()
print("Login Failed")
