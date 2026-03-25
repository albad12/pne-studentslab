import socket
from Guesser import NumberGuesser

IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP,PORT))
ls.listen()
a = NumberGuesser()

while True:
    print("Waiting for clients to the game!!")
    (cs, client_ip_port) = ls.accept()
    a = NumberGuesser()
    print("Client connected to the game!!")

    msg_raw = cs.recv(2000)
    msg = msg_raw.decode()
    print(f"Guess by the client: {msg}")
    response = a.guess(msg)
    cs.send(response.encode())
    if "won" in response:
        break
    cs.close()

