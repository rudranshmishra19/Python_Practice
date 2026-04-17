# Read from input.txt and write into ouptut.txt
try:
    with open("input.txt","r") as infile, open ("output.txt","w") as outfile:
        # Read file line by line 
        for line in infile:
            outfile.write(line)
            print(line,end="")

except FileNotFoundError:
    print("Error:input.txt not found !")            
