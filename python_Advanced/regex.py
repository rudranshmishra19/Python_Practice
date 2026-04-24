def has_digit(s):
    for ch in s:
        if ch in "0123456789":
            return True
    return False

s="h0123456789"
import re
print(bool(re.search(r"[a-zA-z]",s)))

