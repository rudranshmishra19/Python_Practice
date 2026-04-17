# def count_to_three():
#     yield 1
#     yield 2
#     yield 3

# for num in count_to_three():
#     print(num)

squares=(x**2 for x in range(10))

for s in squares:
    print(s)

print(list(squares))
print(list(squares))