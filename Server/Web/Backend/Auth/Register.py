#imports
import sys
import hashlib
import re
#---

#modules
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False


#---

LoginErrors=False
UserCode=00000
AuthFile="../Logins.encrypted"

username=sys.argv[1]
username=''.join([i if ord(i) < 128 else ' ' for i in username])
email=sys.argv[2]
password=hashlib.sha256(sys.argv[3].encode()).hexdigest()
Combined=str(username)+str(email)+str(password)
token=hashlib.sha256(Combined.encode()).hexdigest()
userid=hashlib.sha256((str(username)+str(email)+str(UserCode)).encode()).hexdigest()

if(isValid(email)):
    pass
else:
    LoginErrors=True
    print("invalid email")
    exit



LoginsFile = open(AuthFile, 'r')
Logins= LoginsFile.readlines()
 
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
