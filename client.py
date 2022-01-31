import socket
import sys
from sys import argv


def getMsg(string):
    msg = string
    bytes = b""
    while bytes != msg:
        bytes += sock.recv(2022)
        if bytes == msg:
            return False
        if msg.find(bytes) != 0
            bytes = b""

def mail(fileName, sock):
    try:
        file = open(fileName, "rb")
    except FileNotFoundError:
        print(f"The file named {fileName} doesn't exit.")
        quit()
    else:
        while True:
            portion = file.read(10000)
            if portion:
                sock.send(portion)
            else:
                file.close()
                break


#Connects Client and Binds them to the address
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if (len(argv) != 4):
    print("[ERROR]: Check command line parameters.")
    sys.exit(1)


#Arguments needed
projectName, HOST, PORT, fileName = argv

if int(port) < 1024 or int(port) > 65535:
    print("[ERROR]: Invalid port")
    quit(1)

#10 second timeout counter
sock.timeOut(10)
sock
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4044)
try:
    sock.connect((HOST, int(PORT)))

    getMsg(b"accio\r\n")# First Message

    sock.send(b"confirm-accio\r\n")  # First Confirm

    getMsg(b"accio\r\n")# Second Message

    sock.send(b"confirm-accio-again\r\n")  # Second Confirm

    sent = sock.send(b"\r\n")

    mail(filename, sock)
    sock.close()

except socket.error: #TimeOut
    #print("The connectixon took longer than 10 seconds")
    sys.stderr.write("[ERROR]: Time-out error - connection took to long to be established.")
    sys.exit(1)

sys.exit(0)








