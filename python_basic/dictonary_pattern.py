# Frequency counting 
def count_frequency(items):
    freq={}
    for item in items:
        freq[item]=freq.get(item,0)+1
    return freq

frequency=count_frequency([1,1,2,2,2,3,3,3,3])
print(frequency)

