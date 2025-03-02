import pandas as pd
df = pd.DataFram({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
    })

print("Original DataFrame:")
print(df)

#add
df.loc[len(df)] = ['David', 92]
print('\nDataFrame after adding a new row:')
print(df)

#remove
df = df[df['Name'] != 'Charlie']
print("\nDataFRame after removing 'Charlie':")
print(df)

#update
df.loc[df['Name'] == 'Bob', 'Score'] = 95
print("\nDataFrame after updating Bob's score:")
print(df)
