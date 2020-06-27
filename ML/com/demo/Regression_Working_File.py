import pandas as pd

data = pd.read_csv("C:\\Project\\Files\\Input\\csv\\student-mat.csv", sep=";")
print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
print(data.head())