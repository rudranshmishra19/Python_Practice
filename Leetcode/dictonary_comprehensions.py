# Building on your basic dictonary skills
numbers=[1,2,3,4,5]
# Traditional way
square={}
for x in numbers:
    square[x]=x*x
print(square)    

# Advanced 
squares={x:x*x for x in numbers}
print(squares)  #{1:1,2:4,3:9,4:16,5:25}

#with conditions
even_squares={x:x*x for x in numbers if x%2==0}
print(even_squares) 

# From two list
products=['laptop','mouse','keyboard']
price=[1000,25,75]
product_price={products[i]:price[i] for i in range(len(products))}
print(product_price) 