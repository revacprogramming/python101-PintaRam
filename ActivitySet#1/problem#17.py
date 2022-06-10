from socket import *
from codecs import decode
host = "local host"
port = 5000
bufsize =1024
address = (host, port)
server = socket(AF_INET, SOCK_STREAM)
server.connect(address )
dayandtime = decode(server.recv(bufsize), "ascii")
print(dayandtime)
server.close()