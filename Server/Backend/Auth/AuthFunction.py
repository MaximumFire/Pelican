import sys
import hashlib
import re
import json

AuthFile="../../Logins.encrypted.json"

def Authenticate(token):
    AccountFile = open(AuthFile, 'r')
    AccountDict = json.load(AccountFile)

    for account in AccountDict:
        if(token == AccountDict[account]["token"]):
            id = AccountDict[account]["id"]
            username = AccountDict[account]["username"]
            print("Login as " + str(id) + ":" + username)
            AccountFile.close()
            return True
        else:
            pass
    print("Login Failed")
    AccountFile.close()
    return False


def AuthenticateReturnID(token):
    AccountFile = open(AuthFile, 'r')
    AccountDict = json.load(AccountFile)

    for account in AccountDict:
        uToken = AccountDict[account]["token"]
        if(token == uToken):
            return AccountDict[account]["id"]
        else:
            pass
    print("Login Failed")
    AccountFile.close()
    return ""

def AuthenticateUsername(token):
    AccountFile = open(AuthFile, 'r')
    AccountDict = json.load(AccountFile)

    for account in AccountDict:
        uToken = AccountDict[account]["token"]
        if(token == uToken):
            return AccountDict[account]["username"]
        else:
            pass
    print("Login Failed")
    AccountFile.close()
    return ""