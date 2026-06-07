<<<<<<< HEAD
class machine:
    def __init__(self,products,name,price):
        self.products=products
        self.name=name
        self.price=price



vending_machine=machine(["soda","candy","chips"])
# print(vending_machine.products)
=======
class products:
    def __init__(self,products_name,name,price):
        self.products_name=products_name
        self.name=name
        self.price=price

    def is_available(self):
        return self.stock >0

    def reduce_stock(self,quantity):
        if self.stock >=quantity:
            self.stock-=quantity
            return True
        return False

class Inventory:
    def __init__(self):
        self.products=[]

    def add_product(self,product):
        self.products.append(products)

    def show    


    


vending_machine=machine({"soda":200,"chips":10,"cola":20},"snackMaster",500)
print(vending_machine.products_name)
>>>>>>> 63786cdfbe15414d26a1ef920c3bd0bd39c888ce

