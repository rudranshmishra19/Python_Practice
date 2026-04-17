#for loop
arr=[1,2,3,44,5]
for i in arr:
    print(i,end=' ')
print('')
for x in range (1,5):
    print(x,end=' ')
print(' ')
for x in range(100,1150,200):
    print(x,end=' ')
print(' ')    
#while loop
a=10
while(a!=0):
    print(a,end=' ')
    a-=1
print(' ')    
#break and continue statement    
count=0
while True:
    print(count,end=' ')
    count +=1
    if count>=10:
       break
print(' ')
#print out only the even number
n=10
while n>0:
    if n%2!=0:
        n-=1
        continue
    print(n,end=' ')
    n-=1
#else with for loop 
count =0
while(count<5):
    print(count)
    count+=1
else:
    print("Count value reached %d"%(count))    

#print out 1,2,3,4
for i in range(1,20):
    if i==10:
        continue
    print(i)
else:
    print("i  has been terminated it is not printed")
#Loop through and print out all even numbers from the numbers list in the same order they are received.
#  Don't print any numbers that come after 237 in the sequence.
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]  
for number in numbers:
    #if number is odd or number is less than 237
    if number%2!=0 or number>237:
        continue
    else:
        print(number)
        

  