import socket
from Client0 import Client
IP = "127.0.0.1"
PORT = 8080
c = Client(IP,PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP,PORT))

msg = (input("Enter your number: "))
response = c.talk(msg)
s.send(response.encode())
s.close()