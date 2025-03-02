import pandas as pd
data = {
    'Date': ['2024-01-05', '2024-01-06', '2024-01-07'],
    'Values': [10,20,30]
    }
df=pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
print(df)

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

print(df)
