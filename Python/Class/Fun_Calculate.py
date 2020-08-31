global a
a = 1000
print("Value of A:", a)


def fun1():
    global a
    a = 123
    print("This is the value of Fun1:", a)


fun1()


def func2():
    a = 22
    print("This is the value of Fun2:", a)


func2()


def func3():
    print("This is the value of Fun3:", a)


func3()
print("Out side of function value:", a)
