# Simulate a shopping cart
cart={}
def add_to_cart(product,price,quantity=1):
    # Your task:Complete this function
    cart[product]={
        'quantity':cart.get(product,{'quantity':0})['quantity']+quantity,
        'price':price
    }

def show_cart():
    print("\n Your Cart:")
    total=0
    for product,details in cart.items():
        item_total=details['price']*details['quantity']
        total+=item_total
        print(f"{product}:{details['quantity']}x ${details['price']}=${item_total}")
        

#Test it
add_to_cart('laptop',999) 
add_to_cart('mouse',25,2)
add_to_cart('laptop',999)

show_cart()
