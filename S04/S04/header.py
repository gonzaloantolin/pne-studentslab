from pathlib import Path
# Open the file using Path
file_path = Path("sequences/RNU6_269P.txt")

# Read the file content
content = file_path.read_text()

# Split the content by newline and print the first line (header)
print(content.split('\n')[0])
