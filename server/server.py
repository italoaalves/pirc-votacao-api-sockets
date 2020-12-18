import socket
import threading
import json

from methods import vote, count

HOST = '0.0.0.0'
PORT = 40000
TAM_MSG = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)


def Con_cliente(con, cliente):
    while True:
        request = con.recv(TAM_MSG)
        request = json.loads(request.decode())

        response = methods[request["method"](request["body"])]


if __name__ == "__main__":

   while True:
        try:
            con, cliente = sock.accept()
        except:
            break
        threading.Thread(target=Con_cliente, args=(con, cliente)).start()

    con.close()
