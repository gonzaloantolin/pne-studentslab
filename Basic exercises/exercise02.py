text = "  Hello, World! Welcome to Python Programming.  "
text = text.strip()
print("Stripped:", text.strip())
print("Word count:", len(text.split()))
print("Title case:", text.title())
print("Starts with Hello:", text.startswith("Hello"))
print("Ends with ing.:", text.endswith("ing."))
print("Python position:", text.find("Python"))
print("Joined:", " - ".join(text.split()))
