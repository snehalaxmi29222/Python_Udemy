import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9,10,11,12]
    }
df = pd.DataFrame(data)
print("Missing Data:")
print(df.isna())

df_filled = df.fillna(value=0)
print("DataFrame with missing value filled:")
print(df)

