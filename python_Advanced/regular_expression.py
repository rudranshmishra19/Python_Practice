import re

# email="rudranshmishra111@gmail.com"
# pattern= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# if re.match(pattern,email):
#     print("Valid email")
# else:
#     print("Non valid email")    
#re.findall for finding 
# name="rudransh"
# result=re.findall(r"r",name)
# print(result)
# #resub  to replace 
# result=re.sub(r"world","python","hello world")
# print(result)
# # to split string 
# result=re.split(r"\s","Hii my name is Rudransh")
# print(result)
#Extracting phone number
# text="Contact us at 969-309-4424 or 981-907-4065"
# pattern=r"\d{3}-\d{3}-\d{4}"  #match a phone number in the format xxx-xxx-xxxx
# phone_number=re.findall(pattern,text)
# print(phone_number)

#Checking password strength
# def is_strong_password(password):
#     pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
#     #At least 1 uppercase,1 lowercase,1 digit , 1 special char and 8+ character
#     return bool(re.match(pattern,password))

# print(is_strong_password("Strong@123"))  #Output =True
# print(is_strong_password("Weakpasswrod"))  #Output =True

#validating Dates(DD/MM/YYYY) format
# def is_valid_date(date):
#     pattern=r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$"
#     return bool(re.match(pattern,date))

# print(is_valid_date("31/12/2025"))
# print(is_valid_date("32/12/2025"))

# result=re.search(r'\d+','The price is 42 dollars')
# print(result.group())

# text="Your total is 456$"
# result =re.search(r'\d+',text)
# if result:
#     total=int(result.group()) #convert to integer
#     print(f"The total amount {total}")
# else:
#     print("No number found")  
#   






