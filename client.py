import socket


PORT = 65432
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#Command Line Tool
program = sys.argv[0]
host = sys.argv[1]
port = sys.argv[2]
fileName = sys.argv[3]


@staticmethod
def connectTCP(host: str, port: int, fileName: str):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            return True
    except:
        return False











