def is_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    doubled = s1+s2
    return s2 in doubled

print(is_rotation("abcde","cdeab"))
print(is_rotation("abcde","abced")) #False
