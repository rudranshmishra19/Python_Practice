def order_pizza(size,*toppings,**details):
    print(f"Ordering pizza of {size} size")
    print("\nToppings of Pizza are:")
    for topping in toppings:
        print(f"-{topping}")
        
    print("\nDetails of the order are:")
    for key,value in details.items():
        print(f"- {key}: {value}")


order_pizza("Medium","peproni","olives","sausage","mushrooms","Onions",delivery=True,tip=5,Address="502 Ram Krishan Apt Chheda Road Dombivili East")


