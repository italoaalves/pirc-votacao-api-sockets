import socket
import threading


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

        # methods[request["method"](request["data"])]
        print(cliente, request.decode())


while True:
    try:
        con, cliente = sock.accept()
    except:
        break
    threading.Thread(target=Con_cliente, args=(con, cliente)).start()
con.close()
