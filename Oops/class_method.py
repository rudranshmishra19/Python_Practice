class student:
    school_name="ABC School" #class attribute

    def __init__(self,name):
        self.name=name

    @classmethod
    def change_school(cls,new_name):
        cls.school_name=new_name

#Access via class
student.change_school("XYX School")

s1=student("Ravi")
s2=student("Anita")

print(s1.school_name) #XYZ School
print(s2.school_name) #XYZ School
