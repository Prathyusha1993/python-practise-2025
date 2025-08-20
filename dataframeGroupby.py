import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
}

df = pd.DataFrame(data)

# Group by Department and calculate the average salary
print(df.groupby('Department')['Salary'].mean())

# count employee per department
print(df.groupby('Department')['Name'].count())


# multiple aggregations example
print(df.groupby('Department')['Salary'].agg(['mean', 'sum', 'max','min']))

# apply() function - apply a custom funciton to rows and columns
df['updated Salary'] = df['Salary'].apply(lambda x: x *1.1)
print(df)

# applymap() - apply to entire dataframe  - this is deprecated so using map()
df_upper = df.map(lambda x: str(x).upper() if isinstance(x, str) else x)
print(df_upper)


# common panda interview questions:
# series: 1D labeled array
# dataframe: 2D labeled table

# hhow do you find missing in pandas dataframe?
df.isnull().sum

#How do you remove missing values?
df.dropna()

# how do you fill missing values?
df.fillna(0)  #repalce with 0
# df.fillna(df.mean())

#how do you sort a dataframe?
df.sort_values(by='Salary', ascending=False)

# How do you merge/join DataFrames?
# pd.merge(df1, df2, on="EmployeeID", how="inner")

# What is the difference between merge, join, and concat?
# merge() → SQL-like joins (inner, left, right, outer)
# join() → Join on index
# concat() → Stack DataFrames (row-wise or column-wise)

# How do you get unique values in a column?
df['Department'].unique()

# How do you filter rows based on a condition?
filtered_df = df[df['Salary'] > 60000]

# How do you group data and perform aggregations?
grouped_df = df.groupby('Department').agg({'Salary': ['mean', 'sum'], 'Age': 'max'})

# How do you pivot a DataFrame?
pivoted_df = df.pivot_table(index='Department', values='Salary', aggfunc='mean')

# How do you convert a DataFrame to a dictionary?
dict_df = df.to_dict(orient='records')  # Convert to list of dictionaries

# How do you read/write DataFrames to/from CSV/Excel?
# df.to_csv('output.csv', index=False)
# df.to_excel('output.xlsx', index=False)

# How do you get value counts?
value_counts = df['Department'].value_counts()

# How do you convert a DataFrame to NumPy array?
numpy_array = df.to_numpy()

# How do you get the shape of a DataFrame?
shape = df.shape  # Returns (rows, columns)

# How do you get the data types of columns?
data_types = df.dtypes  # Returns a Series with column names as index and data types as values

# How do you rename columns?
df.rename(columns={'Name': 'Employee Name', 'Salary': 'Annual Salary'}, inplace=True)

# How do you reset the index of a DataFrame?
df.reset_index(drop=True, inplace=True)

# How do you set a column as the index?
df.set_index('Employee Name', inplace=True)

# How do you check for duplicates?
duplicates = df.duplicated()  # Returns a Series indicating duplicate rows

# How do you drop duplicates?
df.drop_duplicates(inplace=True)

# How do you get the first n rows of a DataFrame?
first_n_rows = df.head(3)  # Get first 3 rows

# How do you get the last n rows of a DataFrame?
last_n_rows = df.tail(3)  # Get last 3 rows

# How do you get the summary statistics of a DataFrame?
summary_stats = df.describe()  # Returns summary statistics for numerical columns

# How do you convert a DataFrame to a JSON string?
json_string = df.to_json(orient='records')  # Convert to JSON string

# How do you convert a JSON string to a DataFrame?
# json_data = '[{"Name":"Alice","Age":25,"Salary":50000,"Department":"HR"},{"Name":"Bob","Age":30,"Salary":60000,"Department":"Finance"}]'
# df_from_json = pd.read_json(json_data)

# How do you get the index of a DataFrame?
index = df.index  # Returns the index of the DataFrame

# How do you get the columns of a DataFrame?
columns = df.columns  # Returns the columns of the DataFrame

# How do you get the memory usage of a DataFrame?
memory_usage = df.memory_usage(deep=True)  # Returns memory usage of each column

# How do you convert a DataFrame to a Series?
# series_from_df = df['Annual Salary']  # Convert a single column to a Series

# How do you get the first n characters of a string column?
# df['Employee Name'].str[:3]  # Get first 3 characters of 'Name' column