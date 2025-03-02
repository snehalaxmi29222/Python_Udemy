import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
    'Subject': ['Math','Math','Science','Science'],
    'Score': [85, 90, 88, 92]
}
df2 = pd.DataFrame(data)
pivot_df = df2.pivot(index='Name', columns='Subject', values='Score')
print("Orginal Dataframe:")
print(df2)

print("\nPivoted Dataframe:")
print(pivot_df)