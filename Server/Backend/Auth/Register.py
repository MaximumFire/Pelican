#imports
import sys
import hashlib
import re
import json
from random import choice, randint
from string import ascii_letters,  punctuation
#---


#Var
USERS_PATH="../Backend/StoredUsers/"
AUTHFILE="../Logins.encrypted.json"
userid=0
LoginErrors=False


#modules
def isValid(email): #Checks if the email is valid
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    return False


def emailInUse(email): #Checks if the email is alredy being used
    LoginsFile = open(AUTHFILE, 'r')
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
        if char not in allowed or len(name) <= 3: #Min Lan of username
            return False 
    return True


def checkPass(password): #Make sure the password is long enough
    if len(password) >= 8: #Min lan of password
        return True
    return False


def setTag(): #Set the user tag to allow multiple users with the same name
    return str(randint(1000, 9999))
    

def setIdentifier():
    LoginsFile = open(AUTHFILE, 'r')
    LoginsDict = json.load(LoginsFile)

    if LoginsDict == {}:
        LoginsFile.close()
        return 0
    else:
        LoginsFile.close()
        return len(LoginsDict)


def makeUser(uName, uTag):
    UserFile = open(f"{USERS_PATH}{uName}-{uTag}.txt", "w+")
    UserFile.write(uName)
    UserFile.close()


def saveData(uID, uName, uEmail, uPass, uSalt, uToken, uTag, Identifier): #Save the data into the logins file
    if (LoginErrors):
        exit()
    else:       
        LoginsFile = open(AUTHFILE, "r+")
        data = json.load(LoginsFile)
        new_user = {f"{Identifier}": {"username": uName, "tag": uTag, "email": uEmail, "password": uPass, "salt": uSalt, "id": uID, "token": uToken, "role": "Member", "badges": []}}
       
        makeUser(uName, uTag)

        data.update(new_user)
        LoginsFile.seek(0)
        json.dump(data, LoginsFile, indent=2)
        LoginsFile.close()


def genSalt():
    return ''.join(choice(ascii_letters + punctuation) for _ in range(10))
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

password=sys.argv[3]
if not (checkPass(password)):
    LoginErrors=True
    print("Password To Short")
    exit()
salt = genSalt()
password=hashlib.sha256(f"{sys.argv[3]}{salt}".encode()).hexdigest()

Combined=str(username)+str(email)+str(password)
token=hashlib.sha256(Combined.encode()).hexdigest()

tag=str(setTag())

for char in (str(username)+str(tag)):
    userid += ord(char)
userid = str(userid)

identifier = setIdentifier()

try:
    if (not emailInUse(email)):
        saveData(userid, username, email, password, salt, token, tag, identifier)
        print("Register Success")
except Exception as e:
    print(e)
    pass