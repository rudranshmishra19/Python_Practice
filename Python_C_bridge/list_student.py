# Each student : [Name ,Age, Grade]
# students=[
#     ["Alice",20,"A"],
#     ["Bob",21,"B"],
#     ["Charile",25,"A+"]
# ]
# # Acessing student info
# # 
# print(students[0])
# print(students[1][0])

# # Adding a new student
# students.append(["David",25,"B+"])
# print(students[3])

# Using dictonary
students=[
    {"name":"Alice","age":20, "grade":"A"},
    {"name":"Bob","age":21,"grade":"A+"},
    {"name":"Rudransh", "age":22,"grade":"B+"}
]

# Acessing student info
print(students[0]["name"])
print(students[1]["grade"])


for student in students:
    print(f"Name:{student['name']},Age:{student['age']},Grade:{student['grade']}")
