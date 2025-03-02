import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from joblib import Parallel, delayed

data = {
    'A': np.random.randn(1000000),
    'B': np.random.randn(1000000)
}

'''df = pd.DataFrame(data)
df['Sum'] = df['A'] + df['B']
print(df.head())
'''

def compute_mean(sub_df):
    return sub_df['A'].mean()
chunks = np.array_split(df, indices_or_sections=10)

overall_mean = np.mean(results)
print(f"Ovefall mean of column A: {overall_mean}")
