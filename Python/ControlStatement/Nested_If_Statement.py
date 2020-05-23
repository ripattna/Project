age = int(input("Enter your Age:"))
weight = int(input("Enter your Weight:"))
if age > 18:
    if weight > 50:
       print("You are eligible to donate blood")
    else:
       print("You are not eligible to donate blood as your weight is less than 50 KG")
else:
    ("Age must be greater than 18 to donate blood")