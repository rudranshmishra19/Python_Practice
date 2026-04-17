# name=input("Enter your name :")
# print(f"Good Afternoon {name}")
# #letter 
letter="""
     Dear 'Rudransh'
    you are selected !
    Date =12 -2-2024
"""
print(letter.replace("Rudransh",    "Jeet").replace("12-2-2024","15-03-2025"))

name ="Rudransh is a software  Engineer"
#print(name.find("   "))
# if"  " in name:
#     print("Double space found!")

if name.find("  ")==-1:
    print("Double space not found!")
else:
    print("Double space found!")    
# if name.find(" ")==-1:
#     print("Single space not found!")
# else:
#     print("Single space found!")    
print(name.replace("  "," "))
print(name)   ## string are not immutable 
update_me= "I am learning python programming now,\n\t have completed C programming.\nThankyou"
print(update_me)