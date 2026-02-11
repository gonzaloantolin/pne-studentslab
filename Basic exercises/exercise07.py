student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("Student:", student["name"])
print("Number of subjects:", len(student["subjects"]))
if "PNE" in student["subjects"]:
    print("Enrolled in PNE: True")
print("Databases grade:", student["grades"]["Databases"])
average = sum(student["grades"].values()) / len(student["grades"])
print("Average grade:", round(average, 2))
print("Subject grades:")
for subject, grade in student["grades"].items():
    print(subject, ":", grade)