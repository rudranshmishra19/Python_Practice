try:
    # Attempt to open a file 
    with open ("myfile.text","r") as file:
        content=file.read()
        print(content)

except FileNotFoundError:
    print("Error:The file was not found.Please check the file name or path ")

except Exception as e:
    # Catch any other unexecepted exceptions 
    print(f"An unexpected error occured:{e}")
    

