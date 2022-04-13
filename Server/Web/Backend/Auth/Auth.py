import sys
import hashlib
import re
import json

AuthFile="../Logins.encrypted.json" #File where hashed accounts are stored

username=sys.argv[1] #Requested username, for blank ""
email=sys.argv[2] #Requested email, for blank ""
password=hashlib.sha256(sys.argv[3].encode()).hexdigest() #Requested password, for blank ""
userid=sys.argv[4] #Requested userid, for blank ""


AccountFile = open(AuthFile, 'r') #Open the account list
AccountList = json.load(AccountFile)#Read the json in Account File


#Multiple user accounts are being read as one account => Change storing format
for account in AccountList:
    if(AccountList[account]["id"].lower() == userid.lower() and AccountList[account]["password"] == password) or \
        (AccountList[account]["email"].lower() == email.lower() and AccountList[account]["password"] == password) or \
            (AccountList[account]["username"].lower() == username and AccountList[account]["password"] == password):
        username = AccountList[account]["username"]
        id = AccountList[account]["id"]
        print(f"Login as {id}:{username}")
        exit()
    else:
        pass
print("Login Failed")