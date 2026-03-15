import socket
from P01.Seq1 import Seq

PORT = 8080
IP ="127.0.0.1"# the IP address depends on the machine running the server
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")
lst = [
"ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
"AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
"CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
"CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
"AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"
]
while True:

    print("Waiting for clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().strip().split(" ")

        print(f"Message received: {msg[0]}")

        if msg[0] == "PING":
            print("PING command!")
            response = "OK!\n"
            cs.send(response.encode())
            cs.close()

        elif msg[0] == "GET":
            n = int(msg[1])
            if 0 <= n <= 4:
                print(f"{msg[0]}")
                response = lst[n] + "\n"
                print(lst[n])
                cs.send(response.encode())
                cs.close()

        elif msg[0] == "INFO":
            sequence = msg[1]
            s = Seq(sequence)

            total = len(s)

            A = s.count_base("A")
            C = s.count_base("C")
            G = s.count_base("G")
            T = s.count_base("T")

            pa = (A / total) * 100
            pc = (C / total) * 100
            pg = (G / total) * 100
            pt = (T / total) * 100

            response = (f"Sequence: {s}\n"
                        f"Total length: {total}\n"
                        f"A: {A} ({pa:.1f}%)\n"
                        f"C: {C} ({pc:.1f}%)\n"
                        f"G: {G} ({pg:.1f}%)\n"
                        f"T: {T} ({pt:.1f}%)\n")
            print(response)
            cs.send(response.encode())
            cs.close()

        elif msg[0] == "COMP":
            sequence = msg[1]
            s = Seq(sequence)
            comp = s.complement()
            response = (f"Complement: {comp}\n")
            print(response)
            cs.send(response.encode())
            cs.close()

        elif msg[0] == "REV":
            sequence = msg[1]
            s = Seq(sequence)
            rev = s.reverse()
            response = (f"Reverse: {rev}\n")
            print(response)
            cs.send(response.encode())
            cs.close()

        elif msg[0] == "GENE":
            genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
            gene = msg[1]
            if gene in genes:
                s = Seq()
                s.read_fasta(f"../sequences/{gene}.txt")
                response = str(s) + "\n"
                print(f"Gene requested: {gene}")
                print(response)
                cs.send(response.encode())
            else:
                response = "ERROR\n"
                cs.send(response.encode())
            cs.close()

        else:
            response = "ERROR\n"
            cs.send(response.encode())
            cs.close()