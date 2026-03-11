import socket
from os import close

port = 8080
ip = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((ip,port))
ls.listen()

print("SEQ Server configured!")
i = 0
for n in range(4):
    i = n

get_text = "GET" + " " + i
while True:
    print("Waiting for Clients ... ")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        msg = msg.strip()
        if msg == "PING":
            response = "OK!\n"
            print(f"PING command!\n {response}")
            cs.send(f"{response}".encode())
            cs.close()
        elif msg == "GET"
        else:
            cs.send(f"ECHO:{msg}".encode())
            cs.close()
