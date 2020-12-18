import socket
from os import system, name

options = [quit, ]

HOST = '127.0.0.1'
PORT = 40000
TAM_MSG = 1024

serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)


if __name__ == "__main__":
    while True:
        system('cls' if name == 'nt' else 'clear')
        print("Digital ballot box")
        print('''
            (1) Vote
            (2) Count Votes

            (0) Exit program
            ''')

        opt = int(input('> '))

        system('cls' if name == 'nt' else 'clear')
        request = options[opt]()

        sock.send(str.encode(request))

    sock.close()
