import pandas as pd
import matplotlib
import matplotlib.pylab as plt
# Read dataset and store into DataFrame
cars = pd.read_csv("C:\\Project\\Files\\Input\\csv\\cars.csv")
'''Printing the car data set
print("The hard of Car Dataset:'\n' ", + cars.head(),"'\n'","The tail of car Dataset:'\n'", +  cars.tail())
#Converting the data type of mpg to string'''
cars.mpg=cars.mpg.astype(str)
'''print(cars)systemctl restart systemd-logind.service
print("Printing the cars mpg:'\n'",cars.mpg)
print("The cars mpg type:'\n'",type(cars.mpg))
print("Printing the cars data set shape:'\n'",cars shape)
print(cars.info(null_counts=True))
print("The mean of the car data set is:", cars.mean())
print("The median of the car data set is:",cars.median())
print("The stand deviation of the car dataset is:", cars.std())
print("The max of the car data set is:", cars.max())
print("The min of the car data set is:",cars.min())
print("The count of the car data set is:",cars.count())
print(cars.describe())
#To list the columns in the car dataset
print("The column list available in car data set are:'\n'",list(cars.columns))'''
# Rename the column of "Unnamed" to "model"
cars = cars.rename(columns={'Unnamed: 0': 'model'})
# print(cars.head())
# Dropping unwanted column
# cars=cars.drop(columns=['disp'])
# Feeling the null values with mean of the column
cars.qsec = cars.qsec.fillna(cars.qsec.mean())
# print(cars.head())
# find the co-relation matrix
df = cars[['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']].corr()
# print(df)
# Converting the datatype of mpg from string to float
cars.mpg = cars.mpg.astype(float)
''''#To view the hp column
#print("To view the hp column'\n'",cars.iloc[1:,4])
#print("Print record 6th row onwards and 4th column '\n'", cars.iloc[6:,4:])
#Display the records from index 0 to index 6 from mpg column
print("Display the records from index 0 to index 6 from mpg column:'\n'",cars.loc[:6,"mpg"])
#Select the first 7 records from mpg to qsec column
print("Select the first 7 records from mpg to qsec column:'\n'",cars.loc[:7,"mpg":"qsec"])'''
# Set the column value 1 to the column 'am'
# print("Print before the changes'\n'", cars.am)
# cars['am']=1
# print("Print after changes '\n'",cars.am)
# Double up the value in 'am' using lamda fxn
# f=lambda x: x*2
# cars['2am']=cars['am'].apply(f)
# print(cars['2am'])
# print(cars)
# Sorting cyl column ascending order
# myn = cars.sort_values(by='cyl', ascending=False)
# print(myn)
# Filter records with more than 6 cylinders
# cyld = cars['cyl'] > 6
# print(cyld)
# ######################Data Visualization##########

# %matplotlib inline
y1 = cars['hp']
x1 = range(32)
plt.plot(x1, y1)
plt.show()
