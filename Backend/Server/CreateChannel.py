import os
import sys
import re
import random
import time

sys.path.insert(1, "../Backend/Auth/")
from AuthFunction import Authenticate, AuthenticateReturnID

SERVERS_DIR = "../Backend/Servers/"

serverid=sys.argv[1]
token=sys.argv[2]
username=sys.argv[3]
channelname=sys.argv[4]

if(Authenticate(token)):
    
    if(os.path.isdir(SERVERS_DIR+str(serverid))):
        with open(f"{SERVERS_DIR}{serverid}/ServerInfo.txt", "r+") as f:
            data = f.readlines()
            savedusername = data[1][:-1]
            if username == savedusername:
                os.mkdir(SERVERS_DIR+str(serverid)+"/"+channelname)
                with open(f"{SERVERS_DIR}{serverid}/{channelname}/ChannelInfo.txt", "w+") as f:
                    f.write(f"{channelname}\n{username}")
                print(f"{channelname} created successfully")
            else:
                print(f"{username} is not the owner of this server")
    else:
        print(f"{serverid} is not a valid server")
else:
    print(f"{token} is not valid")

