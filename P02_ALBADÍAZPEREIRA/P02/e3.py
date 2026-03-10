from Client0 import Client

practice = 2
exercise = 3
print(f"-----| Practice {practice}, Exercise {exercise} |------")

ip = "212.128.255.75"
port = 8080
c = Client(ip, port)

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response:{response}")