# How to create a dataframe
import pandas as pd
import numpy as np

data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)
print("The type of df:", type(df))

# Creating a DataFrame using dictionary
dictionary = {'fruit': ['apple', 'banana', 'mango'], 'count': [10, 20, 15]}
df_new = pd.DataFrame(dictionary)
print(df_new)

# Creating a DataFrame using series
series = pd.Series([6, 12], index=['a', 'b'])
df_new1 = pd.DataFrame(series)
print(df_new1)

# Creating a DataFrame using numpy array
num = np.array([[5000, 4000], ['John', 'James']])
df = pd.DataFrame({'name': num[1], 'salary': num[0]})
print(num)
