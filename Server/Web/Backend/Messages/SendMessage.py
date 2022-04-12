from http import server
import sys
import random
import re
import time

message=sys.argv[1]
serverid=sys.argv[2]
channelid=sys.argv[3]
token=sys.argv[4]

import sys
sys.path.insert(1, '../Auth/')
from AuthFunction import Authenticate;

if(Authenticate(token)):

    messageid=""
    #---
    #Generate message id by message as base64, channelid, serverid+random number up to 999999999
    #messageid=
    for c in message:
        messageid=str(messageid)+str(ord(c))

    messageid=re.sub("[^0-9]", "",messageid+channelid+serverid+str(random.randint(0,9999))+str(time.time()))
    print(messageid)


    if(os.path.isdir("../../../Servers/"+str(serverid))):
        if(os.path.isdir(f"../../../Servers/{serverid}/{channelid}")
            with open(f"../../../Servers/{serverid}/{channelid}/Messages.log", "a+") as f:
                f.write(f"{message}")
                f.close()
        else:
            print("Channel ID Does Not Exist")
            exit
    else:
        print("Server ID Does Not Exist")
        exit
        
else:
    print("NO AUTH")