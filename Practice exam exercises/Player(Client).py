import socket

IP = "127.0.0.1"
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP,PORT))

while True:
    msg = (input("Enter your number: "))
    s.send(msg.encode())
    response = s.recv(2048).decode()
    print(f"Server says: {response}")
    if "won" in response:
        break
s.close()