import socket
from Seq1 import Seq

port = 8080
ip = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((ip,port))
ls.listen()

seqs = [ "AATGTCGGCCCA",
         "TGTGATGATGATGC",
         "ATGCGTCGCGCGTAGTAGTATG",
         "ATGTGATGTGGTC"]

seqs2 = {"U5": "Sequences/U5_sequence.fa",
        "ADA": "Sequences/ADA_sequence.fa",
        "FRAT": "Sequences/FRAT1_sequence.fa",
        "FXN": "Sequences/FXN_sequence.fa",
        "RNU6_269P": "Sequences/269P_sequence.fa"}

while True:
    print("Waiting for Clients ... ")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        msg = msg.strip()
        parts = msg.split(" ", 1)
        comd = parts[0]
        if comd == "PING":
            response = "OK!\n"
            print(f"PING command!\n {response}")
            cs.send(f"{response}".encode())
        elif comd == "GET":
            index = int(parts[1])
            seq = seqs[index]
            print(f"GET\n {seq}")
            cs.send(f"{seq}".encode())
            print()
        elif comd == "INFO":
            s = parts[1]
            seq = Seq(s)
            bases = seq.count_dict()
            response = f"Sequence: {seq}\n Total length: {seq.len()}\n"
            for base, count in bases.items():
                percentage = (count / seq.len()) * 100
                response += f"{base}: {count} % \n"
            print(response)
            cs.send(response.encode())
        elif comd == "COMP":
            s = parts[1]
            seq = Seq(s)
            print(f"COMP\n {seq.complement()}")
            cs.send(f"{seq.complement()}".encode())
            print()
        elif comd == "REV":
            s = parts[1]
            seq = Seq(s)
            print(f" REV\n {seq.reverse()}")
            cs.send(f"{seq.reverse()}".encode())
            print()
        elif comd == "GENE":
            gene = parts[1]
            if gene in seqs2:
                seq = Seq()
                seq.read_fasta(seqs2[gene])
                result = seq.strbases
                print(f"GENE\n {result}")
                cs.send(f"{result}".encode())
        else:
            cs.send(f"ECHO:{msg}".encode())
    cs.close()
