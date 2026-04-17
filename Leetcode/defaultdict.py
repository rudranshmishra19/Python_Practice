from collections import defaultdict
d=defaultdict(list)
d['a'].append(1) #No keyError!
d['b'].append(2)
d['c'].append(1)
print(d)