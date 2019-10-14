import socket
import base64

# Задаем адрес сервера
SERVER_ADDRESS = ('localhost', 12391)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')

# Слушаем запросы
while True:
    try:
        connection, address = server_socket.accept()
        print("new connection from {address}".format(address=address))

        data = connection.recv(1024)
        print(base64.b64decode(data.decode('utf-8')).decode('utf-8'))
        while True:
            cmd = input('CMD> ')
            if cmd == 'exit':
                break
            connection.send(base64.b64encode(cmd.encode('utf-8')))
            data = connection.recv(1024)
            print(base64.b64decode(data.decode('utf-8')).decode('utf-8'))

        connection.close()
    except:
        break

server_socket.close()
