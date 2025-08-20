import pandas as pd

# read csv file
df = pd.read_csv('employee.csv')

# reade xcel file:
df_excel = pd.read_excel('employee.xlsx')

# write dataframe to csv
df.to_csv('output.csv', index=False)
print(df.head())  #shows first 5 rows of the dataframe

# read  only specific columns from a csv
df_specific = pd.read_csv('employee.csv', usecols=['Name', 'Salary'])

# read firsy 100 rows
df = pd.read_csv('employee.csv', nrows=100)

