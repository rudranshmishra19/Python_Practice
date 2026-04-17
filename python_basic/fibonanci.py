def fibonaci(num):
    fib0=0
    fib1=1
    if num<=0:
        return "fibonaci series not defined for non-positvie numbers"
    if num ==1:
        print("Fib series : 0")
        return 0
    elif num==2:
        print("Fib series :0 1")
        return 1
    print("Fibonacci series:",end=' ')
    print(fib0,fib1, end=" ")
    for i in range(2,num):
         fibNext=fib1+fib0  # 1+0 = 1  
         print(f"{fibNext}",end=" ")
         fib0=fib1  # 
         fib1=fibNext # 1
    print()     
    return fibNext     


         
num=(int(input("Enter how many terms of fibonnaci series you want  :")))
print(f"The fibonacci series upto given number is {fibonaci(num)}")