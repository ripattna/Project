try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("only +ve int are allowed")
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")

except ValueError as e:
    print e
except:
    print("something is wrong")

