import pandas as pd
#read cars.csv into a dataframe with a delimiter as ;
cars = pd.read_csv('cars.csv', delimiter=';')
#check the shape of the data
print(cars.shape)
#print first 5 rows of the data
print(cars.head())
#print last 5 rows of the data
print(cars.tail())
#print the columns
print(cars.columns)
#print the data types
print(cars.dtypes)
#print the summary statistics
print(cars.describe())
#print the unique values of the origin column
print(cars['origin'].unique())




