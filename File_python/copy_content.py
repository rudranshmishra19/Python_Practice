def copy_file(source,destination):
    with open (source,'r') as src:
        with open(destination,'w') as dest:
            for line in src:
                dest.write(line)

#Example usage
source_file="myfile.txt"
destination_file="destination.txt"

if destination_file:
    print("file sucessfully created")
else:
    print("file creation failed")    

def append_to_file(filename,text):
    with open(filename,'a') as file:
        file.write(text +"\n")  #adds a newline after the text

#Example usage
filename="myfile.txt"
append_to_file(filename,"This is new text added at the end ")
print("Text appended Sucessfully ")
