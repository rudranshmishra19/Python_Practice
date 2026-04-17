def fibonaci(num):
    fib0=0
    fib1=1
    series=[]
    if num<=0:
        return "fibonaci series not defined for non-positvie numbers"
    if num >=1:
        series.append(fib0)
       
    if num >=2:
        series.append(fib1)
         
    for i in range(2,num):
         fibNext=fib1+fib0  # 1+0 = 1  
         series.append(fibNext)
         fib0=fib1  # 
         fib1=fibNext # 1
    return series    


         
num=(int(input("Enter how many terms of fibonnaci series you want  :")))
result=fibonaci(num)
if isinstance(result,str):
    print(result)
else:    
    print(f"The fibonacci series with {num} terms is:{result} ")