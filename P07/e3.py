import http.client
import json


from e2 import genes

SERVER = "rest.ensembl.org"
gene_name = "MIR633"
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

print(f"GENE: {gene_name}")
print(f"Description: {response["desc"]}")
print(f"Bases: {response["seq"]}")