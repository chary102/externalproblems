def rev(s):
    if len(s) == 0:
        return s
    else:
        return rev(s[1:])+ s[0]
a = input("Enter the string: ")
print(rev(a))
