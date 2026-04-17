def fibonnaci_generator():
        fib0,fib1=0,1
        while True:
                yield fib0 #provide the current value 
                fib0,fib1=fib1,fib0+fib1 #update to next iteraton

#prompt user for input
n=(int(input("Enter the Nthserise: ")))
if n<=0:
        print("Pls enter a positive integer")
else:
    #generate the fibonacii series
    fib_gen=fibonnaci_generator()
    fib_seires=[next(fib_gen)for _ in range(n)]
    print(f"The Nth series is {', '.join(map(str,fib_seires))}")


                

