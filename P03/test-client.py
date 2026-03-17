from Client0 import Client

ip = "127.0.0.1"
port = 8080

client = Client(ip, port)
commands = ["PING", "GET", "INFO", "COMP", "REV", "GENE"]
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

get0 = ""

for comd in commands:
    print(f"* TESTING {comd}...")

    if comd == "PING":
        response = client.talk(comd)
        print(response.strip(), "\n")

    elif comd == "GET":
        for j in range(5):
            get_cmd = f"{comd} {j}"
            seq = client.talk(get_cmd).strip()
            print(f"{comd} {j}: {seq}")
            if j == 0:
                get0 = seq
        print()

    elif comd in ["INFO", "COMP", "REV"]:
        response = client.talk(f"{comd} {get0}").strip()
        if comd != "INFO":
            print(f"{comd} {get0}")
        print(response, "\n")

    elif comd == "GENE":
        for name in genes:
            gene_cmd = f"{comd} {name}"
            server_gen = client.talk(gene_cmd).strip()
            print(gene_cmd)
            print(server_gen, "\n")
