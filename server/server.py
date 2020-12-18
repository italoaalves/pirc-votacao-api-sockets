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
    print("cliente conectado ", cliente)

    while True:
        request = con.recv(TAM_MSG)
        request = json.loads(request.decode())

        method = request["header"]["method"]
        data = request["body"]

        response = options[str(method)](data)

        if request["header"]["method"] == "vote":
            print(f'Voto para o candidato {request["body"]["candidate"]} Registrado' if response["status"] == "success" else "Falha")

        con.send(str.encode(json.dumps(response)))


if __name__ == "__main__":
    while True:
        try:
            con, cliente = sock.accept()
        except:
            break

        threading.Thread(target=Con_cliente, args=(con, cliente)).start()

    con.close()
