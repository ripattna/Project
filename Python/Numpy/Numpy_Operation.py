###Numpy delete element from array
import numpy as np
x=np.arange(1,10)
print('X:',x)
y=np.delete(x,3)
print('Y:',y)
z=np.delete(x,[3,5,8])
print('Z:',z)
a=np.delete(x,np.s_[5:8])
print('A:',a)