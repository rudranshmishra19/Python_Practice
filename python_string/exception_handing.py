my_list=[1,2,3]
try:
    my_list[5]=0
except IndexError:
    print("my_list[5] not found")
        