import numpy as np
import pandas as pd

data = {
    'A': [1,2,3],
    'B': [4,5,6],
    'C': [7,8,9]
}

df = pd.DataFrame(data)
result_df = df.applymap(lambda x: x*2)
print("original dataframe:")
print(df)
print("\nDataFrame after applying function with applymap:")
print(result_df)

sum_by_column = df.apply(sum)
print(sum_by_column)
