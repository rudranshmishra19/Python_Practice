class student:
    # name of the school
    school_name="ABC School"  

    def __init__(self,name):
        self.name=name
    # method to change the cls
    @classmethod
    def change_school(cls,new_name):
        cls.school_name=new_name

    @staticmethod
    def is_adult(age):
        return age>=18    

s1=student("Rohan")

print(student.is_adult(20))  #True
print(student.is_adult(15))  #False

print(s1.school_name)