import socket
import argparse
import json
from settings import HOST, PORT, BUFFERSIZE, ENCODING

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODING

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('address', nargs=1, type=str)
    parser.add_argument('port', nargs='*', type=int)
    args = parser.parse_args()
    if args.address:
        host = args.address[0]
    if args.port:
        port = args.port[0]
except:
    pass

try:
    sock = socket.socket()
    sock.connect((host, port))
    sock.send(json.dumps({'action': 'presence'}).encode(encoding))
    request = json.loads(sock.recv(buffersize), encoding=encoding)
    print(request)
    sock.close()
except KeyboardInterrupt:
    print('Client closed')
