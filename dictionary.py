student={
    "name":"Arsath",
    "age":21,
    "major":"AIDS"
    }
print(student)
print(student["name"])
print(student.get("age"))
student["age"]=22
student["grade"]="A"
print(student)
print("Keys:",student.keys())
print("Values:",student.values())
print("Items:",student.items())
for key,value in student.items():
    print(key,":",value)
for key in student.keys():
    print(key)
for value in student.values():
    print(value)
print(student.get("salary","Not Available"))
removed_value=student.pop("major")
student={
    "name":"Alice",
    "age":21,
    "subjects":["Math","Physics","Computer science"]
    }
print(student["name"])
print(student["subjects"][0])
#Dictionary inside list
students=[
    {"name":"Alice","age":21},
    {"name":"Bob","age":22}
    ]
print(students[0]["name"])
print(students[1]["age"])
