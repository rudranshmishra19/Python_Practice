# phonebook={}
# phonebook["jeet"]=1122939343
# phonebook["Omkar"]=4502032230
# phonebook["Pankaj"]=1122948343
# print(phonebook)

# alternate ways to initalize dictonary
phonebook={
     "Jeet"  :9534304034,
     "Omkar"  :969453033,
     "Pankaj" :4993493434
}
#print(phonebook)

for name,number in phonebook.items():
    print("phone number of %s is %d"%(name,number))
del phonebook["Jeet"]     # use to delete a value 
#or 
phonebook.pop("Pankaj")

print(" ")
for name,number in phonebook.items():
    print("phone number of %s is %d"%(name,number))
