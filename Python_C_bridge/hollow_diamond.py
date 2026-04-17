rows=(int(input("Enter the number of rows :")))
for i in range(rows):
    for k in range(rows+1-i):
        print(" ",end="")
    for j in range(2*i-1):
        if j==1 or j==2*i-1:
            print("* ",end="")
        else:
            print(" ")    
    print()    
for i in range(rows,-1,-1):
    for k in range(rows+1-i):
        print(" ",end="")
    for j in range(i+1):
        
        print("* ",end="")
    print()    