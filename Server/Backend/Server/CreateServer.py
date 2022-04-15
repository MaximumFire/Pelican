import os
import sys
import re
import random
import time

sys.path.insert(1, "../Backend/Auth/")
from AuthFunction import Authenticate, AuthenticateReturnID

SERVERS_DIR = "../Backend/Servers/"

servername=sys.argv[1]
token=sys.argv[2]
username=sys.argv[3]

if(Authenticate(token)):
    ServernameInt=0
    usernameint=0
    for c in servername:
        ServernameInt=str(ServernameInt)+str(ord(c))
    for c in username:
        usernameint=str(usernameint)+str(ord(c))

    serverid=re.sub("[^0-9]", "",str(ServernameInt)+str(usernameint)+str(random.randint(0,9999))+str(time.time()))

    if(os.path.isdir(SERVERS_DIR+str(serverid))):
        print("Server Exists, Wait 1 Second and retry")
        exit()
    else:
        os.mkdir(SERVERS_DIR+str(serverid))

        with open(f"{SERVERS_DIR}{serverid}/ServerInfo.txt", "a+") as f:
            f.write(f"{serverid}\n{username}\n{servername}")
            f.close()
        with open(f"{SERVERS_DIR}{serverid}/BannedUsers.txt", "a+") as f:
            f.write(f"")
            f.close()
        with open(f"{SERVERS_DIR}{serverid}/InvitedUsers.txt", "a+") as f:
            f.write(f"{AuthenticateReturnID(token)}\n")
            f.close()
else:
    print("NO AUTH")