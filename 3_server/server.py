import socket
import argparse
import json
from settings import HOST, PORT, BUFFERSIZE, ENCODING

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODING

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', type=str,
                    help='Sets network address')
parser.add_argument('-p', '--port', type=int,
                    help='Sets port')

args = parser.parse_args()

if args.address:
    host = args.address
if args.port:
    port = args.port

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    while True:
        client, address = sock.accept()
        query = client.recv(buffersize)
        try:
            query = json.loads(query, encoding=encoding)
            if query['action'] == 'presence':
                client.send(json.dumps({'responce': 200, "alert": "Everything ok"}).encode(encoding))
                client.close()
            else:
                raise ValueError
        except:
            client.send(json.dumps({'responce': 400, "error": "Something goes wrong. Again"}).encode(encoding))
            client.close()
except KeyboardInterrupt:
    print('Server closed')