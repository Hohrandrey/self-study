student = {"name": "Anna", "age": 20, "grade": "B"}
student.update({"grade" : "A", "city" : "Moscow"})
del student["age"]
print(student)