def fact1(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def fact_recur(n):
    if n==0:
        return 1
    else:
        return n * fact_recur(n-1)

a = int(input("enter +ve int value :"))
print "fact of ", a, "is ", fact1(a)
print "fact of using recursion ", a, "is ", fact_recur(a)




    
