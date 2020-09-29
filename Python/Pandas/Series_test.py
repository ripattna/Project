import pandas as pd

data = [1, 2, 3, 4]
series1 = pd.Series(data)
print(series1)
# Changing the index of a series Object
series1 = pd.Series(data, index=['a', 'b', 'c', 'd'])
print("##############")
print(series1)

