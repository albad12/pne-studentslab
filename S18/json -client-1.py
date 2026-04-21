import http.client

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")
conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", "/")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")

print(f"Content: {data1}")
