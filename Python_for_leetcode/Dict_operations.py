inventory={'apple':10,'banana':5,'orange':8}

inventory['apple']=inventory.get('apple',0)+3
print("After adding apples:",inventory)

# Loop through items and print stock
print("\nCurrent stock")
for key,value in inventory.items():
    print(f" product {key}:{value}units ")

banana_count=inventory.pop('banana')
print(f"\nRemoved {banana_count} bananas")
print("Inventory after removal:", inventory)

# Task 4:Check if grapes exits(without error)
grape_stock=inventory.get('grapes',0)

print(f"Grape stock:{grape_stock}")

