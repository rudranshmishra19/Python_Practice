try:
    huge = [0] * (10**12)  # bahut zyada memory maang raha hai
except MemoryError:
    print("Memory nahi hai, kuch objects delete karo")