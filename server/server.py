import socket
import threading
import json

from methods.vote import vote
from methods.count import count

HOST = '0.0.0.0'
PORT = 40000
TAM_MSG = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)

options = {
    "vote": vote,
    "count": count
}


def Con_cliente(con, cliente):
    while True:
        request = con.recv(TAM_MSG)
        request = json.loads(request.decode())

        response = options[str(request["header"]["method"])](request["body"])

        con.send(str.encode(json.dumps(response)))


if __name__ == "__main__":
    while True:
        try:
            con, cliente = sock.accept()
        except:
            break

        threading.Thread(target=Con_cliente, args=(con, cliente)).start()

    con.close()
