import sys
import hashlib
import re

AuthFile="../../../Logins.encrypted"

username=sys.argv[1]
email=sys.argv[2]
password=hashlib.sha256(sys.argv[3].encode()).hexdigest()
token=sys.argv[4]



AccountFile = open(AuthFile, 'r')
AccountList = AccountFile.readlines()

    # Username[1], 
for account in AccountList:
    AccountInfo=account.split(":")
    if(AccountInfo[0].lower()==username.lower() and AccountInfo[4]==password or AccountInfo[3].lower()==email.lower() and AccountInfo[4]==password or token == AccountInfo[5]):
        print(f"Login as {AccountInfo[0]}:{AccountInfo[1]}")
    else:
        pass
print("Login Failed")