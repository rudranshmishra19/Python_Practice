def count_lines_word(filename):
    line_count=0
    word_count=0
    
    with open(filename,'r') as file:
        for line in file:
            line_count+=1
            words=line.split()
            word_count+=len(words)

    return line_count,word_count

#Example usage
filename="myfile.txt"
lines,words=count_lines_word(filename)
print(f"Lines:{lines}")        
print(f"Words:{words}")        