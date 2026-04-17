# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass

#     def get_pass(self):
#         return self.__acc_pass
        

# acc1=Account(12333,"aeferer")
# print(acc1.acc_no)
# # get method to print password
# print(acc1.get_pass())

class Person:
    __name="anonymous"

    def __hello(self,name):
        print("Hello person")

    def welcome(self):
        self.__hello()

p1=Person()
print(p1.__name)
print(p1.welcome())




 