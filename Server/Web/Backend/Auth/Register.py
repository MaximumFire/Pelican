#imports
from pickletools import TAKEN_FROM_ARGUMENT1
import sys
import hashlib
import re
import json
#---

LoginErrors=False



#Var
AuthFile="../Logins.encrypted.json"
tag=0000
userid=0


#modules
def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    return False

def emailInUse(email):
    LoginsFile = open(AuthFile, 'r')
    LoginsDict = json.load(LoginsFile)

    for user in LoginsDict:
        if (LoginsDict[user]["email"].lower() == email.lower()):
            LoginErrors=True
            print("Email already in use")
            LoginsFile.close()
            exit()
    LoginsFile.close()
    return False

def checkName(name):
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for char in name:
        if char not in allowed or len(name) < 3:
            return False 
    return True

def nameInUse(name):
    LoginsFile = open(AuthFile, 'r')
    LoginsDict = json.load(LoginsFile)

    for user in LoginsDict:
        if (LoginsDict[user]["username"].lower() == name.lower()):
            LoginErrors=True
            print("Username already in use")
            LoginsFile.close()
            exit()
    LoginsFile.close()
    return False

def checkPass(password):
    if len(password) > 7:
        return True
    return False

def setUserCode():
    LoginsFile = open(AuthFile, 'r')
    LoginsDict = json.load(LoginsFile)

    for user in LoginsDict:
        if (LoginsDict[user]["username"].lower() == username.lower()):
            usercode+=1
    LoginsFile.close()
    return usercode

def saveData(uID, uName, uCode, uEmail, uPass, uToken, uTag):
    if (LoginErrors):
        exit()
    else:       
        usercode = uCode
        LoginsFile = open(AuthFile, "r+")
        data = json.load(LoginsFile)
        new_user = {f"{usercode}": {"username": uName, "tag": uTag, "email": uEmail, "password": uPass, "id": uID, "token": uToken}}
        data.update(new_user)
        LoginsFile.seek(0)
        json.dump(data, LoginsFile)
        LoginsFile.close()


#---

username=sys.argv[1]
if not (checkName(username)):
    LoginErrors=True
    print("Invalid Username")
    exit()

email=sys.argv[2]
if not (isValid(email)):
    LoginErrors=True
    print("Invalid Email")
    exit()

# Is it secure to check the unhashed password like this?
password=sys.argv[3]
if not (checkPass(password)):
    LoginErrors=True
    print("password too short")
    exit()

password=hashlib.sha256(sys.argv[3].encode()).hexdigest()
Combined=str(username)+str(email)+str(password)
token=hashlib.sha256(Combined.encode()).hexdigest()
usercode = setUserCode()

for char in (str(username)+str(usercode)):
    userid += ord(char)


LoginsFile = open(AuthFile, 'r')
LoginsFile = json.load(LoginsFile)
    
try:
    if (not nameInUse(username) and not emailInUse(email)):
        saveData(userid, username, usercode, email, password, token, tag)
        print("Register Success")
except Exception as e:
    print(e)
    pass