from time import perf_counter
a=list(range(10000))
b=list(range(10000))
t1=perf_counter()
c=[e1+e2 for e1,e2 in zip(a,b)]
t2=perf_counter()
print("add list :%f sec" % (t2-t1))
##Numpy list performance
import numpy as np
x=np.array(a)
y=np.array(b)
t1=perf_counter()
z=x+y
t2=perf_counter()
print("add np array:%f sec" % (t2-t1))