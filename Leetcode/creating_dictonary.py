my_dict={}
# Dictonary with some values
student={
    "name":"Rudransh",
    "age":23,
    "Course":"python"
}
 

student["grade"]="A"
student["Batch"]=11
student.pop("Batch")
student.popitem()



#Loop key-value pairy
# for key,value in student.items():
#     print(key,value)
print(student)