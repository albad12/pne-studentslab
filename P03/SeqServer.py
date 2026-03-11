import socket
from Seq1 import Seq

port = 8080
ip = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((ip,port))
ls.listen()

seqs = [ "AATGTCGGCCCA", "TGTGATGATGATGC", "ATGCGTCGCGCGTAGTAGTATG", "ATGTGATGTGGTC"]
seqs2 = {"U5": "Sequences/U5_sequence.fa",
        "ADA": "Sequences/ADA_sequence.fa",
        "FRAT": "Sequences/FRAT1_sequence.fa",
        "FXN": "Sequences/FXN_sequence.fa",
        "RNU6_269P": "Sequences/269P_sequence.fa"}

s = Seq()

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
        msg = msg.strip().split(" ", 1)
        comd = msg[0]
        if msg == "PING":
            response = "OK!\n"
            print(f"PING command!\n {response}")
            cs.send(f"{response}".encode())
            cs.close()
        elif comd == "GET":
            seq = seqs[int(msg[1])]
            print(f"GET\n {seq}")
            cs.send(f"{seq}".encode())
            print()
            cs.close()
        elif comd == "INFO":
            msg[1] = input()
            s = msg[1]
            seq = Seq(s)
            bases = seq.count_dict()
            for value, key in bases.items():
                print(f"Sequence: {seq}\n Total length: {seq.len()}\n {key}: {value}: {(value / seq.len) * 100} %")
                cs.send(f"Sequence: {seq}\n Total length: {seq.len()}\n {key}: {value}: {(value / seq.len) * 100} %".encode())
                cs.close()
        elif comd == "COMP":
            sq = input()
            msg[1] = sq
            seq = Seq(sq)
            print(f"COMP\n {seq.complement()}")
            cs.send(f"{seq.complement()}".encode())
            print()
            cs.close()
        elif comd == "REV":
            sq = input()
            msg[1] = sq
            seq = Seq(sq)
            print(f" GET\n {seq.reverse()}")
            cs.send(f"{seq.reverse()}".encode())
            print()
            cs.close()
        elif comd == "GENE":
            for key, value in seqs2.items():
                seq = seqs2[str(msg[1])]
                print(f"GENE\n {seq}")
                cs.send(f"{seq}".encode())
                print()



        else:
            cs.send(f"ECHO:{msg}".encode())
            cs.close()
