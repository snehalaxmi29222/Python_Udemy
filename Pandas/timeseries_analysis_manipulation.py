import pandas as pd

data={
    'Date': ['2024-01-01', '2024-01-10', '2024-01-15'],
    'Values': [10,20,30,40,50]
    }

df=pd.DataFrame(data)
df.set_index('Date', inplace=True)

monthly_df = df.resample('M').mean()
print(monthly_df)

df['Rolling_Mean']=df['Value'].rolling(window=2).mean()
print(df)


