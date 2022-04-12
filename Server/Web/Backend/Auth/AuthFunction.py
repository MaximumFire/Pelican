import sys
import hashlib
import re

AuthFile="../../../Logins.encrypted"
def Authenticate(token):
    AccountFile = open(AuthFile, 'r')
    AccountList = AccountFile.readlines()

        #Username[0], Usercode[1], Usercode[2], Email[3], Password[4], Token[5]
    for account in AccountList:
        AccountInfo=account.split(":")
        if(token == AccountInfo[4]):
            print(f"Login as {AccountInfo[0]}:{AccountInfo[1]}")
            return True
        else:
            pass
    print("Login Failed")
    return False