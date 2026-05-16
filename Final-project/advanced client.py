import requests

url = "http://localhost:8080/listSpecies?limit=5&json=1"
req = requests.get(url)
print("LIST SPECIES")
print(req.json())
print()

url = "http://localhost:8080/karyotype?species=human&json=1"
req = requests.get(url)
print("KARYOTYPE")
print(req.json())
print()

url = "http://localhost:8080/chromosomeLength?species=human&json=1"
req = requests.get(url)
print("CHROMOSOME LENGTH")
print(req.json())
print()

url = "http://localhost:8080/geneLookup?gene=BRCA2&json=1"
req = requests.get(url)
print("GENE LOOKUP")
print(req.json())
print()

url = "http://localhost:8080/geneSeq?gene=BRCA2&json=1"
req = requests.get(url)
print("GENE SEQ")
print(req.json())
print()

url = "http://localhost:8080/geneInfo?gene=BRCA2&json=1"
req = requests.get(url)
print("GENE INFO")
print(req.json())
print()

url = "http://localhost:8080/geneCalc?gene=BRCA2&json=1"
req = requests.get(url)
print("GENE CALC")
print(req.json())
print()

url = "http://localhost:8080/geneList?chromo=9&start=22125500&end=22136000&json=1"
req = requests.get(url)
print("GENE LIST")
print(req.json())
print()