from P01.Seq1 import Seq
import http.client
import json
from e2 import genes

SERVER = "rest.ensembl.org"
gene_name = input("Write the gene name: ").upper()
gene_id = genes[gene_name]

ENDPOINT = "/sequence/id/" + gene_id
PARAMS = "?content-type=application/json"


print()
print(f"Server: {SERVER}")
print(f"URL: {SERVER + ENDPOINT + PARAMS}")

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
data = response.read().decode("utf-8")
response = json.loads(data)
def composition(s):
    total = len(s)
    A = s.count_base("A")
    C = s.count_base("C")
    G = s.count_base("G")
    T = s.count_base("T")

    pa = (A / total) * 100
    pc = (C / total) * 100
    pg = (G / total) * 100
    pt = (T / total) * 100

    response = (f"A: {A} ({pa:.1f}%)\n"
                f"C: {C} ({pc:.1f}%)\n"
                f"G: {G} ({pg:.1f}%)\n"
                f"T: {T} ({pt:.1f}%)\n")
    print(response)

sequence = response["seq"]
s = Seq(sequence)
bases_dict = s.count()
most_frequent = max(bases_dict, key=bases_dict.get)
print(f"GENE: {gene_name}")
print(f"Description: {response["desc"]}")
print(f"Length: {len(s)}")
print(f"Most frequent Base: {most_frequent}")
composition(s)