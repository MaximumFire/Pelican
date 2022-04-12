import sys
import hashlib
import re

AuthFile="../../../Logins.encrypted" #File where hashed accounts are stored

username=sys.argv[1] #Requested username, for blank ""
email=sys.argv[2] #Requested email, for blank ""
password=hashlib.sha256(sys.argv[3].encode()).hexdigest() #Requested password, for blank ""
token=sys.argv[4] #Requested token, for blank ""
userid=sys.argv[5] #Requested userid, for blank ""



AccountFile = open(AuthFile, 'r') #Open the account list
AccountList = AccountFile.readlines() #Read the lines in the account list

for account in AccountList:
    AccountInfo=account.split(":")
    if(AccountInfo[0].lower()==userid.lower() and AccountInfo[4]==password or AccountInfo[3].lower()==email.lower() and AccountInfo[4]==password or token == AccountInfo[5] or AccountInfo[1].lower()==username.lower() and AccountInfo[4]==password):
        print(f"Login as {AccountInfo[0]}:{AccountInfo[1]}")
    else:
        pass
print("Login Failed")