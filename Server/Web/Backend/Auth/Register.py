#imports
from pickletools import TAKEN_FROM_ARGUMENT1
import sys
import hashlib
import re
#---

#modules
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
        return True
    return False

def checkName(name):
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for char in name:
        if char not in allowed or len(name) < 3:
            return False 
    return True

def checkPass(password):
    if len(password) > 8:
        return True
    return False

#---

LoginErrors=False
UserCode=00000
AuthFile="../Logins.encrypted"

#1. Bug: Input Error, ex.: If user enters 'super man' as username, 'man' gets set as email and program throws an email error
# Suggestion: 
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
userid=hashlib.sha256((str(username)+str(email)+str(UserCode)).encode()).hexdigest()


LoginsFile = open(AuthFile, 'r')
Logins= LoginsFile.readlines()

#2. Bug: User login will fail if multiple users are stored in this format at Logins.encrypted
# Suggestion: Store data in multidimensional-dictionaries with key-value pairs (?)
for account in Logins:
    try:
        AccountDetails=account.split(":")
        if(username.lower()==AccountDetails[1].lower()):
            UserCode+=1
        else:
            pass
        if(email.lower()==AccountDetails[3].lower()):
            LoginErrors=True
            print("email already used")
            exit
        else:
            pass
    except:
        pass
LoginsFile.close()


if(LoginErrors):
    exit
else:
    LoginsFile=open(AuthFile,'a')
    #UserID[0], Username[1], Usercode[2], Email[3], Password[4], Token[5]
    LoginsFile.write(str(userid)+":"+str(username)+":"+str(UserCode)+":"+str(email)+":"+str(password)+":"+str(token))
    LoginsFile.close()
    print("Register Success")
