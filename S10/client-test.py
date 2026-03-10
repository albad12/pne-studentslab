from Client0 import Client
import socket

ip = "212.128.255.75"
port = 8080

count = 0
c = Client(ip,port)
for:
    response = c.talk(f"Message{count}")
    print(f"To Server: Message{count}")
    print()
    print(f"From Server: ECHO: Message {response}")
    response = c.talk(f"{cs}")
    print(f"To server:{cs}")
    print(f"From Server:\n {response}")