#imports
from pickletools import TAKEN_FROM_ARGUMENT1
import sys
import hashlib
import re
import json
#---

LoginErrors=False
AuthFile="../Logins.encrypted.json"

#modules
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
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
            exit
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
            exit
    LoginsFile.close()
    return False

def checkPass(password):
    if len(password) > 8:
        return True
    return False

def setUserCode():
    LoginsFile = open(AuthFile, 'r')
    LoginsDict = json.load(LoginsFile)
    if LoginsDict == {}: # no users added yet
        usercode = 0
    else:
        usercode = len(LoginsDict) + 1
    LoginsFile.close()
    return usercode


def saveData(uID, uName, uCode, uEmail, uPass, uToken):
    if (LoginErrors):
        exit
    pass
    #Need solution here to append user data in right format to the JSON file
    usercode = uCode
    LoginsFile = open(AuthFile, "r+")
    data = json.load(LoginsFile)
    new_user = {f"{usercode}": {"username": uName, "email": uEmail, "password": uPass, "id": uID}}
    data.update(new_user)
    LoginsFile.seek(0)
    json.dump(data, LoginsFile)
    LoginsFile.close()


#---

username=sys.argv[1]
if not (checkName(username)):
    LoginErrors=True
    print("invalid username")
    exit

email=sys.argv[2]
if not (isValid(email)):
    LoginErrors=True
    print("invalid email")
    exit

# Is it secure to check the unhashed password like this?
password=sys.argv[3]
if not (checkPass(password)):
    LoginErrors=True
    print("password too short")
    exit
password=hashlib.sha256(sys.argv[3].encode()).hexdigest()

Combined=str(username)+str(email)+str(password)
token=hashlib.sha256(Combined.encode()).hexdigest()

usercode = setUserCode()
userid=hashlib.sha256((str(username)+str(email)+str(usercode)).encode()).hexdigest()


LoginsFile = open(AuthFile, 'r')
LoginsFile = json.load(LoginsFile)
    
try:
    if (not nameInUse(username) and not emailInUse(email)):
        saveData(userid, username, usercode, email, password, token)
        print("Register Success")
except Exception as e:
    print(e)
    pass


# for account in Logins:
#     try:
#         AccountDetails=account.split(":")
#         if(username.lower()==AccountDetails[1].lower()):
#             UserCode+=1
#         else:
#             pass
#         if(email.lower()==AccountDetails[3].lower()):
#             LoginErrors=True
#             print("email already used")
#             exit
#         else:
#             pass
#     except:
#         pass
# LoginsFile.close()


# if(LoginErrors):
#     exit
# else:
#     LoginsFile=open(AuthFile,'a')
#     #UserID[0], Username[1], Usercode[2], Email[3], Password[4], Token[5]
#     LoginsFile.write(str(userid)+":"+str(username)+":"+str(UserCode)+":"+str(email)+":"+str(password)+":"+str(token))
#     LoginsFile.close()
#     print("Register Success")
