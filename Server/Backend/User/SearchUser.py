import sys
import re
from os import listdir
from os.path import isfile, join


USERS_PATH="Server/Backend/StoredUsers/"
users = [f for f in listdir(USERS_PATH) if isfile(join(USERS_PATH, f))]
users = [f[:-4] for f in users]

#--
def isValid(username):
    regex = re.compile(r'[A-Za-z0-9]+[:]+[0-9]{4,4}')
    if re.fullmatch(regex, username):
        return True
    return False
#--

username = sys.argv[1]
if isValid(username):
    name = username.replace(':', '-')
else:
    print("not valid")
    exit()
for user in users:
    if user == name:
        print("User was found")
        exit()
print("User was not found")
