l=[2,3,4,5,6,7,8,9,10]
for i in l:
    my_lamda=lambda x:(x%2)==1
    print(f"{i} is odd:{my_lamda(i)}")