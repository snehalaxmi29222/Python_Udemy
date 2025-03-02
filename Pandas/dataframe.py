import pandas as pd
data = {
    'name': ['alice', 'bob', 'smith'],
    'age': [25,30,35],
    'city': ['New York', 'Los Angles', 'Chicago']
    }
df = pd.DataFrame(data)
print(df)
