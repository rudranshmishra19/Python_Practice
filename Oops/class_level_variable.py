class student:
    #class level vairable 
    school_name="ABC School"

    def __init__(self,name,age):
        #instance -level variables
        self.name=name
        self.age=age

s1=student("Rohan",16)
s2=student("Aman",17)

print(s1.school_name) #ABC school
print(s2.school_name) #ABC school 
print(student.school_name) #ABC School 