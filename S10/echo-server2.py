import socket
import termcolor

port = 8080
ip = "212.128.255.75"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((ip,port))
ls.listen()
print("The server is configured!")

count = 1
while True:
    print("Waiting for Clients to connect")
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
        print(f"Connection{count}: {client_ip_port}")
        print(f"Received Message: {msg}")

        cs.send(f"ECHO: {msg}".encode())
        cs.close()
        count += 1