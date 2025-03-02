import pandas a pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25,30,34,45],
    'Salary': [5000,6000,7000,8000]
    }
df = pd.dataFrame(data)

#filtering
filtered_df = df[df['Age'] > 30]
print(filtered_df)


#sorting
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df)

#grouping
df['Department'] = ['HR', 'Finance', 'HR', 'Marketing']
grouped_df = df.group_by('Department')['Salary'].mean()
print(grouped_df)
