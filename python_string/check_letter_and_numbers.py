# s="geeksforgeeks1"
# # Check if the 's' contains at least one letter
# l=any(c.isalpha() for c in s)
# n=any(c.isdigit() for c in s)

# if l and n:
#     print(True)
# else:
#     print(False)

# Using built in string method like set.isdisjoint()

s="geeksforgeeks"
has_letter=not set(s).isdisjoint(set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
has_digit=not set(s).isdisjoint(set('0123456789'))

if has_digit and has_letter:
    print(True)
else:
    print(False)
    