# def http_error(status):
#     match status:
#         case 400 |403|404:
#             return "Bad Request"
#         case 200:
#             return "ok"
#         case 201:
#             return "created"
#         case 401:
#             return "Unauthorized Error"
#         case _:
#             return "Something's wrong with the internet"


# print(http_error(400))

# point is an (x,y) tuple
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# def where_is(point):
#     match point:
#         case Point(x=0,y=0):
#             print("Origin")
#         case Point(x=0,y=y):
#             print(f"Y={y}")
#         case Point(x=x,y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")

# p=Point(x=9,y=0)
# where_is(p)



