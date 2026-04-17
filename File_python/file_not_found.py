import os
filename="data.txt"
try:
    with open ("data.txt","r") as f: #file does not exists
       content=f.read()
     
except FileNotFoundError:
    print(f"{filename} not found.Creating a new file.....")
    with open (filename,"w") as f:
        f.write("Hii i been absoultely nothing for two years \n")

# Check if file really exists 
if os.path.exists(filename):
    print("File is sucessfully created ")
else:
    print("File is not created ")             