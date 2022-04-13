import sys
import hashlib
from AuthFunction import Authenticate

username=sys.argv[1] #Requested username, for blank ""
email=sys.argv[2] #Requested email, for blank ""
password=hashlib.sha256(sys.argv[3].encode()).hexdigest() #Requested password, for blank ""
userid=sys.argv[4] #Requested userid, for blank ""

Combined=str(username)+str(email)+str(password)
token=hashlib.sha256(Combined.encode()).hexdigest()

Authenticate(token)
