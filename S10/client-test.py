from Client0 import Client


ip = "212.128.255.75"
port = 8080


c = Client(ip,port)
for i in range(5):
    response = c.talk(f"Message{i}")
    print(f"To Server: Message{i}")
    print(f"From Server: ECHO: Message {response}")
