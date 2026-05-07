# t=(1,2,3)
# s={4,5,6}
# d={"a":1,"b":2}

# print(list(t))
# print(list(s))
# print(list(d))
# print(list(d.values()))
# print(list(d.items()))

# To tuple
# l=[1,2,3]
# s={4,5,6}
# d={"a":1,"b":2}
# print(tuple(l))
# print(tuple(s))
# print(tuple(d))
# print(tuple(d.items()))

# To set
# l=[1,2,2,3]
# t=(("age",23),)
# d={"a":1,"b":2}
# print(set(l))
# print(set(t))
# print(set(d))
# print(d.values())

# To Dict
# From list/tuple of pairs
# pairs=[("a",1),("b",2)]
# print(dict(pairs))

# From two separate lists using zip
# keys=["a","b","c"]
# values=[1,2,3]
# print(dict(zip(keys,values)))

# Using dict comprehension
# l=[1,2,3]
# print({x:x**2 for x in l})

# Conversion that is not allowed 
# s={1,2,3}
# print(dict(s))
# Dict ->set(loses data)
# d={"a":1,"b":2}
# print(set(d))

# Dict set loses data 
# d={"a":1,"b":2}
# print(set(d))

# print(dict([("a",1),("b",2)]))
# # Fails not pairs
# # print(dict([1,2,3]))
# print(dict(["ab","cd"]))
# s={3,1,2}
# print(list(s))

# s={[1,2]:"value"}
# print(s)
# Tuple as dict key -Works
# d={(1,2):"value"}
# print(d)

