import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Values': [10, 20, 30]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
print(df)


df['Date'] = pd.to_datetime(df['Date'])
print(df)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

print(df)
