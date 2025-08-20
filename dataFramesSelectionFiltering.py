import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
}

df = pd.DataFrame(data)
print(df['Name'])
print(df[['Name', 'Salary']])
print(df[df['Age'] > 25])
print(df.iloc[0:3])  #select first 3 rows
print(df.iloc[1])   #select second row by index
print(df.loc[0])        #select first row by label 
print(df.loc[df['Department'] == 'IT'])  #select rows where Department is IT