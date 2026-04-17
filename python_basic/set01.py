my_list=[1,2,3,4]
my_set=set(my_list)
print(my_set)
# my_dict={value: index for index ,value in enumerate(my_list)}
my_dict=dict(zip(my_list,range(len(my_list))))

print(my_dict)
