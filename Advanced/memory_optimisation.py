import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['A', 'B', 'C'] * 100000,
    'Value': np.random.randn(300000),
    'ID': np.arange(300000)
}

df = pd.DataFrame(data)

print("Original memory usage:")
print(df.memory_usage(deep=True).sum())

df['Category'] = df['Category'].astype('category')
df['ID'] = df['ID'].astype('int32')

print("\nOptimized meonry usage:")
print(df.memory_usage(deep=True).sum())