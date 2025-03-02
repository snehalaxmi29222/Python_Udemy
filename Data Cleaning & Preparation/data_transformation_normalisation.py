import pandas as pd
import numpy as np

data2 = {'Score': [120, 50, 100, 200, 500]}

df2 = pd.DataFrame(data2)

df2 = pd['Normalised_Score'] = (df2['Score']-df2['Score'].min()) / (df2['Score']-df2.max())

print("\nOringinal dataframe:")
print(df2)

print("\nDataframe after Min-Max Normalisation")
print(df2[['Score', 'Normalised_Score']])








          