from pathlib import Path
file_path = Path("sequences/U5.txt")
content = file_path.read_text()
lines = content.split("\n")
for line in lines[1:]:
    print(line)
    