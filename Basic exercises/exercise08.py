students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

def average(grades):
    return sum(grades) / len(grades)

def get_status(avg):
    if avg >= 5.0:
        return "PASS"
    else:
        return "FAIL"

passed = 0
failed = 0

for student in students:
    avg = average(student["grades"])
    status = get_status(avg)

    print(student["name"], ":", round(avg, 1), "->", status)

    if status == "PASS":
        passed += 1
    else:
        failed += 1

print("Total Passed:", passed)
print("Total Failed:", failed)

