def maxi(num):
    greater=num[0]
    for i in num:
        if i>greater:
            greater=i
    return greater    

num=[1,2,3,4,5]
maximum=maxi(num)
print(maximum)