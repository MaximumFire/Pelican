import sys
import datetime

command = str(sys.argv[1])

with open("logs/shell_logs.txt", "a+") as log:
    log.write(command+"\n");

log.close()