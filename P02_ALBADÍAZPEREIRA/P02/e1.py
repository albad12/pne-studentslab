from Client0 import Client

practice = 2
exercise = 1

print(f"-----| Practice {practice}, Exercise {exercise} |------")

ip = "212.128.255.75"
port = 8080

c = Client(ip, port)
c.ping()