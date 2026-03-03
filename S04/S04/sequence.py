from pathlib import Path
file_path = Path("sequences/ADA.txt")
content = file_path.read_text()
lines = content.split('\n')
lines = lines[1:]
total_bases = 0
for line in lines:
    total_bases += len(line)
print(total_bases)
