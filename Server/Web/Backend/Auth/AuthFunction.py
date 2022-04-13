import sys
import hashlib
import re

AuthFile="../../../Logins.encrypted"
def Authenticate(token):
    AccountFile = open(AuthFile, 'r')
    AccountList = AccountFile.readlines()

    for account in AccountList:
        AccountInfo=account.split(":")
        if(token == AccountInfo[5]):
            print(f"Login as {AccountInfo[1]}:{AccountInfo[2]}")
            return True
        else:
            pass
    print("Login Failed")
    return False


def AuthenticateReturnID(token):
    AccountFile = open(AuthFile, 'r')
    AccountList = AccountFile.readlines()

    for account in AccountList:
        AccountInfo=account.split(":")
        if(token == AccountInfo[5]):
            return AccountInfo[0]
        else:
            pass
    print("Login Failed")
    return ""

#Hey this needs to be fixed with the new json format!