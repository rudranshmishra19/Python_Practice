n=5
for i in range(5):
    for k in range(n+1-i):
        print(" ",end="")
    for j in range(i+1):
       # if j==
        print(f"{j}",end=" ")
    print()    
for i in range(5,-1,-1):
    for k in range(n+1-i):
        print(" ",end="")
    for j in range(i+1):
        
        print("* ",end="")
    print()    