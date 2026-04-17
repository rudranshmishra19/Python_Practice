marks ={
    "Aman":85,
    "Riya":92,
    "kabir":78,
    "Neha":90
}
k=3
# sort element by 2 highest rank
sorted_items=sorted(marks.items(),key=lambda x:x[1], reverse=True)
print(sorted_items)
result=[key for key, values in sorted_items[:k]]
print(result)

# print(marks.items())
# print(marks.get("Aman"))
# print(marks.get("a",0))
# print(marks.values())
# print(marks.keys())
