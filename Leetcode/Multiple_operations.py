def dictionary_operations():
    my_dict={}

    # Adding values
    my_dict['apple']=1
    my_dict['banana']=3
    my_dict['cherry']=6

    print("After adding:",my_dict)

    # Checking if key exists
    print("'apple ' in dict:", 'apple' in my_dict) #True
    print("'orange' in dict:",'orange' in my_dict) #False


    # Accesssing values
    print("Value for 'banana':",my_dict ['banana']) #2

    # Updating value 
    my_dict['banana']=5
    print("After update:",my_dict)

dictionary_operations()
