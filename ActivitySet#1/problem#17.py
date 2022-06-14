""""from socket import *
from codecs import decode
host = "local host"
port = 5000
bufsize =1024
address = (host, port)
server = socket(AF_INET, SOCK_STREAM)
server.connect(address )
dayandtime = decode(server.recv(bufsize), "ascii")
print(dayandtime)
server.close() """"



from socket import *

mysock = socket(AF_INET, SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()