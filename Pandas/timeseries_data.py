import pandas as pd
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Values': [10,15,7, 22, 17]
    }
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Data'])
df.set_index('Date', inplace=True)
print(df)

monthly_df = df.resample('M').mean()
print(monthly_df)
