def reverse(s):
    str1 = ""
    for i in s:
        str = i + str1
    return str1


s = "Geeksforgeeks"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
