import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
    'Age': [25,None,30,22]
    'City': ['New York', 'Los Angles', None, 'Chiacogo']
    }
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

cleaned_df = df.dropna()
print("\nDataFrame after dropping missing values:")
print(cleaned_df)

filled_df = df.fillna('Age': df['Age'].mean(), 'City': 'Unknown')
print("\nDataFRame after filling missing values:")
print(filled_df)

