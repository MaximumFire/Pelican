import os
import sys
import re
import random
import time

sys.path.insert(1, "../Backend/Auth/")
from AuthFunction import Authenticate, AuthenticateReturnID

SERVERS_DIR = "../Backend/Servers/"

username = sys.argv[1]

# NEEDS MORE WORK