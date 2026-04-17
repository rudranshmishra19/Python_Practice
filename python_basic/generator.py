# #Normal function
# def get_number():
#     return [1,2,3,4,5]

# print(get_number())

# Generator - Yeilds one at a time
def get_numbers():
    yield 1
    yield 2
    yield 3

get_numbers()
for num in  get_numbers():
    print(num)

