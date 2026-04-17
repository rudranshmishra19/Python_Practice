# Method in Dic
my_dict={'a':1,'b':2,'c':3}

# 1.get() safe value access
result=(my_dict.get('a',0))+1
print(result)

print(my_dict.get('a',0))
# .keys() Get all keys
print(my_dict.keys())


# .values()-Get all values 
print(my_dict.values())

# 4 .get key-values pair
for key,value in my_dict.items():
    print(f"{key} :{value}")
    
