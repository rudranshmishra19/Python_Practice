from collections import defaultdict
groups=defaultdict(list)
list=['cat','act','hat','stops','posts']     
for words in list:
    print("printing",words)
    str="".join(sorted(words))
    groups[str].append(words)
    print("printing sorted words",str)
    print(groups)
