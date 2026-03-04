import socket


PORT = 8081
IP = "212.128.255.75"

while True:
# -- Ask the user for the message
    message = str.encode(input("Enter the message: "))
# -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Establish the connection to the Server
    s.connect((IP, PORT))
# -- Send the user message
    s.send(message)
# -- Close the socket
    s.close()

