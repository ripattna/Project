global a
a = 1000
'''def calculate(a,b):
    print("The Sum:", a+b)
    print("The Difference:", a-b)
    print("The Product:", a*b ) 
calculate(200,10)'''


def fun1():
    global a
    a = 222
    print("This is the value of Fun1:", a)


fun1()


def func2():
    a = 22
    print("This is the value of Fun2:", a)


func2()


def func3():
    print("This is the value of Fun3:", a)


func3()
print("This is outside of function!")
