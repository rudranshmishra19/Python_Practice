# Recurrsive approach for elements
def sum(lst,index):
     if index==0:
          return lst[index]
     
     return lst[index] + sum(lst,index-1)
     

lst=[1,5,6,7]   
result=sum(lst,3)
print(result)


#12+7=19