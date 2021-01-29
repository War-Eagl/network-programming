# This file receives the request from client side and 
# displays the website

from socket import *
from os import path

server_port = 8000

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',server_port))

server_socket.listen(1)

print('The server is ready to receive')

while 1:
    connection_socket, client_address = server_socket.accept()
    message = connection_socket.recv(1024)
    filename = message.split()[1]
    print(filename[1:])
    if path.exists(filename[1:]):
        with open(filename[1:]) as f:
            webpage = f.read()
    else:
        print('error 404')
        with open('error404.html') as f:
            webpage=f.read()
    print(webpage)
    webpage = b'HTTP/1.1 200 OK\r\n Content-Type: text/html\r\n' + webpage
    connection_socket.send(webpage)
    connection_socket.close()