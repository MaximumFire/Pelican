#imports
import sys
import hashlib
import re
import json
#---


#Var
AuthFile="../Logins.encrypted.json"
userid=0
LoginErrors=False


#modules
def isValid(email): #Checks if the email is valid
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    return False

def emailInUse(email): #Checks if the email is alredy being used
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

def checkName(name): #Check that the name is the corrent lan and no illegal characters
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for char in name:
        if char not in allowed or len(name) < 3:
            return False 
    return True


def checkPass(password): #Make sure the password is long enough
    if len(password) > 7:
        return True
    return False

def setUserCode(): # gets identifier for the key (to put as the key in json)
    LoginsFile = open(AuthFile, 'r')
    LoginsDict = json.load(LoginsFile)

    if LoginsDict == {}: # no users added yet
        usercode = 0
    else: # some users added, so make it 1 more than last (starts at 0 so it will be len(LoginsDict))
        usercode = len(LoginsDict)
    
    LoginsFile.close()
    return usercode

def setTag(): #Set the user tag to allow multiple users with the same name
    tag=0
    LoginsFile = open(AuthFile, 'r')
    LoginsDict = json.load(LoginsFile)

    for user in LoginsDict:
        if (LoginsDict[user]["username"].lower() == username.lower()):
            tag+=1
    LoginsFile.close()
    return tag

def saveData(uID, uName, uCode, uEmail, uPass, uToken, uTag): #Save the data into the logins file
    if (LoginErrors):
        exit()
    else:       
        LoginsFile = open(AuthFile, "r+")
        data = json.load(LoginsFile)
        new_user = {f"{tag}": {"username": uName, "tag": uTag, "email": uEmail, "password": uPass, "id": uID, "token": uToken, "role": "Member", "badges": []}}
        data.update(new_user)
        LoginsFile.seek(0)
        json.dump(data, LoginsFile, indent=2)
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
    print("Password To Short")
    exit()

password=hashlib.sha256(sys.argv[3].encode()).hexdigest()
Combined=str(username)+str(email)+str(password)
token=hashlib.sha256(Combined.encode()).hexdigest()
tag=str(setTag())

usercode = str(setUserCode())

for char in (str(username)+str(tag)):
    userid += ord(char)
userid = str(userid)


LoginsFile = open(AuthFile, 'r')
LoginsFile = json.load(LoginsFile)
    
try:
    if (not emailInUse(email)):
        saveData(userid, username, usercode, email, password, token, tag)
        print("Register Success")
except Exception as e:
    print(e)
    pass