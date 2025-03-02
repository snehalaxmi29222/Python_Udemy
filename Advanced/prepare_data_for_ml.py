import pandas as pd
import numpy as np
'''data = {
    'Age': [25, 30, np.nan, 45, 50, 1000],
    'Salary': [500000, 60000, 65000, np.nan, 70000, 120000]
}

df = pd.DataFrame(data)

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

df = df[df['Age'] <= 90]
print(df)
'''

data = {
    'Height_cm': [160, 175, 180],
    'Weight_kg': [55, 80, 75]
}

df = pd.DataFrame(data)

df['BMI'] = df['Weight_kg'] / (df['Height_cm'] / 100) ** 2
print(df)


