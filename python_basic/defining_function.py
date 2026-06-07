# def fib(n):
#     """print fibonnacic series"""
#     result=[]
#     a,b=0,1
#     while a<n:
#         result.append(a)
#         a,b=b,a+b
#     return result

# print(fib(10))

# Default arguments
def prompt(problem,token=10,response='haha what you are doing'):
    while True:
        output=input(problem)
        if output in {'200','201','202'}:
            print("OK")
            return True
        if output in {'400','401','404'}:
            print("error")
            return False
        token-=1
        if token==0:
            raise ValueError('you have used your limit')
        print(response)    


f=prompt("how much can you see:" )
