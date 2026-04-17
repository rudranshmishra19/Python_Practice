class NegativeNumberError(Exception):
     pass

def square_root(num):
    if num <0:
        raise NegativeNumberError(num)
    return num**0.5

# Example usage
try:
    print(square_root(45))
    print(square_root(-9))
except NegativeNumberError as e:
    print("Error:",e)

    
       

        