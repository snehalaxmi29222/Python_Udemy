import numpy as np
import pandas as pd
df1 = pd.DataFrame({
    'ID': [1,2,3],
    'Name': ['Jenny', 'Charlie', 'Alice']
})
df2 = pd.DataFrame({
    'ID': [1,2,4],
    'Score': [85,90,89]
})

merged_df = pd.merge(df1, df2, on='ID')

print("Merged dataframe on 'ID': ")
print(merged_df)