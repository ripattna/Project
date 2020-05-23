#Creating a DataFrame using numpy array
import numpy as np
import pandas as pd
num = np.array([[5000,4000],['John','James']])
df=pd.DataFrame({'name':num[1],'salary':num[0]})
#print("num", num)
print("df", df)