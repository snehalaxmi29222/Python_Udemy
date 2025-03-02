import numpy as np
import pandas as pd

data = {'Name': ['alice', 'bob', 'alice', 'charlie', 'bob'],
        'Age': [25, 30, 25, 35, 30]
        }
df = pd.DataFrame(data)
print("Original DataFrame:", df)

df_no_duplicates = df.drop_duplicates(subset='Name')
print(df_no_duplicates)

df2 = pd.DataFrame(data)
