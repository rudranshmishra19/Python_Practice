#Example 1:Direct proof
s1="hello"
print(f"Original ID:{id(s1)}") #Memory address
s1=s1+"word" #seems like modification
print(f"After 'modification':{id(s1)}") #Different memory address!

s1_upper=s1.upper()
print(f"s.upper():{id(s1_upper)}")