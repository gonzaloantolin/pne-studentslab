import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

print()
print(f"Server: {SERVER}")
print(f"URL: {SERVER + ENDPOINT + PARAMS}")


conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
data = response.read().decode("utf-8")
response = json.loads(data)

if response["ping"] == 1:
    print("ALIVE!")