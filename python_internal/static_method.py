# class MathUtils:
#     @staticmethod
#     def add(a,b):
#         return a +b

# print(MathUtils.add(3,5))

class User:
    def __init__(self,age):
        self.age=age
    @staticmethod
    def is_valid(age):
        return 0 <age<150


print(User.is_valid(44))
