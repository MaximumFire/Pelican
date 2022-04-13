import sys

command = sys.argv[1]

try:
    with open("shell_logs.txt", "a+") as log:
        log.write(command+"\n");
except:
    log.write("error at SaveLogs.py")

log.close()