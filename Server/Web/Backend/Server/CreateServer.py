import os
import sys
import re
import random
import time

import sys
sys.path.insert(1, '../Auth/')
from AuthFunction import Authenticate;


servername=sys.argv[1]
username=sys.argv[2]
token=sys.argv[3]

if(Authenticate(token)):
    ServernameInt=0
    usernameint=0
    for c in servername:
        ServernameInt=str(ServernameInt)+str(ord(c))
    for c in username:
        usernameint=str(usernameint)+str(ord(c))

    serverid=re.sub("[^0-9]", "",str(ServernameInt)+str(usernameint)+str(random.randint(0,9999))+str(time.time()))

    if(os.path.isdir("../../../Servers/"+str(serverid))):
        print("Server Exists, Wait 1 Second and retry")
        exit
    else:
        os.mkdir("../../../Servers/"+str(serverid))

        with open(f"../../../Servers/{serverid}/ServerInfo.txt", "a+") as f:
            f.write(f"{serverid}\n{username}\n{servername}")
            f.close()
        with open(f"../../../Servers/{serverid}/BannedUsers.txt", "a+") as f:
            f.write(f"")
            f.close()
        with open(f"../../../Servers/{serverid}/InvitedUsers.txt", "a+") as f:
            f.write(f"")
            f.close()
else:
    print("NO AUTH")