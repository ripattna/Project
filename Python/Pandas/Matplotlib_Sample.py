import pandas as pd
import matplotlib.pylab as plt
cars = pd.read_csv("C:\\project\\Python\\cars.csv")
# Rename the column of "Unnamed" to "model"
cars = cars.rename(columns={'Unnamed: 0':'model'})
# print(cars.describe())
print(cars.head())
#########################
y1 = cars['hp']
y2 = cars['disp']
x = range(32)
plt.plot(x, y1)
plt.plot(x, y2)
# plt.legend()
# plt.show()
plt.plot(x, y1, linewidth=2.0, color='C')
plt.stackplot(x, y1, color='purple', alpha=0.7)
plt.plot(x, y2, linewidth=1.0, color='r')
plt.stackplot(x, y2, color='black', alpha=0.5)
# plt.show() #Print the area plot
###########
x1 = cars['model'].tolist()
# Adding fingure to adjust figsize
fig = plt.figure(figsize=(30, 15))
# See how hp changes with bar plot
# plt.bar(x1,y1,color='purple', alpha=0.8)
plt.barh(x1, y1, color='purple', alpha=0.8)
plt.show()