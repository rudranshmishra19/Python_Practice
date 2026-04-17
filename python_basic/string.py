# a="Rudransh"
# b="Mishra"
# print(",".join([a,b]))
# print(",".join([a,b]))

# x="Python"
# y="is"
# z="awesome"
# a="but"
# b="c"
# c="is"
# d="my"
# e="first"
# f="language"


# #with space delimiter
# print(" ".join([x,y,z,a,b,c,d,e,f]))

# To split string
# text="Rudransh,Mishra,Mumbai"
# print(text.split(","))

# #split with space
# text="Python is awesome"
# print(text.split(" "))

# text ="hello     world"
# # print(text.split(" "))
# # Leading/trailing space
# # print(text.split( ))
# print(text.split(" "))

# Captialize in python

# text="rudransh mishra"
# # capitalize -only first letter of enitre string
# print(" ".join([ x.capitalize() for x in text.split()]))

# text="rudransh Mishra"
# #step 1 -split into list
# words=text.split()
# print(words)

# #step 2 -capitalize each word
# capitalized=[x.capitalize() for x in words]
# print(capitalized)
# result=" ".join(capitalized)
# print(result)

# number=42
# print("%d" % number)
# print("%d" %number)
# print("{number}".format(number=number))

# name="Rudransh"
# if name == "Jhon":
#     pass

# name="Jhon"
# # How do you use a ternary operator ??
# result ="Jhon" if name== "Jhon" else"Jane"
# print(result)

# How do you use a while loops
# count=0
# while count<5:
#     print(count)
#     count+=1

# a=['foo','bar','baz']
# while True:
#     if not a:
#         break
#     print(a.pop())
# a=['foo','bar','baz']
# for True:
#     if not a:
#       break
   
# for n in range(1,10):
#     print(n)
# 
# 

# a=2
# b=3
# while a<10:
#     b+=a
#     print(b)
#     a+=2
#     print(a)
# print(b)

# def factorial(n):
#     if n == 0 or n ==1:
#         return 1
#     return n* factorial(n-1)
# print(factorial(5))

# def factorial(n):
#     result =1
#     for i in range(1,n+1):
#         result*=i
#     return result
# print(factorial(5))


add = lambda x,y: x+y
print(add(3,4))
