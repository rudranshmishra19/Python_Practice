# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# sequence =my_generator()
# print(next(sequence))   

# gen=my_generator()
# print(next(sequence))    
# print(next(sequence)) 

#Generating a sequence of numbers   
# def generate_numbers(n):
#     for i in range(n):
#         yield i

# gen=generate_numbers(5)
# print(list(gen))

#Generator expression 
# gen_exp=(x**2 for x in range(1,8))
# print(next(gen_exp))
# print(next(gen_exp))

#Comparison with list comphernsion
# square_list=[x**2 for x in range(1,5)]
# print(square_list)  

# square_gen=(x**2 for x in range(1,5))
# print(next(square_gen))
# print(next(square_gen))

#Lazy_Evaluation
def infinite_sequence():
    num=0
    while True:
        yield num
        num+=1
gen=infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))

