import sys
sys.path.insert(1, '../Auth/')
from AuthFunction import Authenticate;

token=sys.argv[4]

if(Authenticate(token)):
    pass
else:
    print("NO AUTH")