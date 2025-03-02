import pandas as pd
data = {
    'Name': ['Jenny', 'John', 'Smith', 'Alice'],
    'Age': [25,30,35,40],
    'City': ['Chicago', 'Los Angles' 'New York', 'Miami']
    }
df = pd.DataFrame(data)
age_column = df['Age']
print("Selected 'Age' coulumn:")
print(age_column)
name_city = df[['Name', 'City']]
print("\nSelected 'Name' and 'City' columns:")
print(name_city)

