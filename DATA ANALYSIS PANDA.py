"""
1-how big is your data set
2what are the names of the columns
ans:shapes and columns
"""
import pandas as pd 

data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)
print(df)
print(f'shape: {df.shape}')
print(f'columns: {df.columns}')
print(f'first row: {df.iloc[0]}')
print(f'second row: {df.iloc[1]}')


