# class Square:
#     def __init__(self,area):
#         self.area=area
#         print(f"{self.area}")

# s=Square(25)
# s.area-=19
# print(s)


# @property ke saath
class Square:
    def __init__(self,area):
        self.area=area
    
    @property
    def area(self):
        return self.area
    
    @area.setter
    def area(self,value):
        self.value=value

s=Square(40)
print(s.area)
