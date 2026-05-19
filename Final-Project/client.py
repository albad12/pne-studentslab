import http.client
import json

SERVER = "127.0.0.1"
PORT = 8080

print("\nCLIENT\n")

while True:
    path = input("\nEnter endpoint: ")

    try:
        conn = http.client.HTTPConnection(SERVER, PORT)
        conn.request("GET", path)

        response = conn.getresponse()

        print("\nResponse:", response.status, response.reason)

        data = response.read().decode("utf-8")

        if "json=1" in path:
            info = json.loads(data)

            print("\nCONTENT:\n")
            for key in info:
                print(key, ":", info[key])
        else:
            print("\nContent:\n")
            print(data)

    except KeyboardInterrupt:
        print("\nClient closed by user")
        conn.close()

