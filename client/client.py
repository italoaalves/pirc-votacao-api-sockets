import socket

HOST = '127.0.0.1'
PORT = 40000
TAM_MSG = 1024
serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)

while True:
    msg = input('> ')
    sock.send(str.encode(msg))
sock.close()
