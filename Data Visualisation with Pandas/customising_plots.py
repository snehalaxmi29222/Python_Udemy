import pandas as pd
import matplotlib.pyplot as plt

'''data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sales': [200, 250, 150, 300, 220]
}

df = pd.DataFrame(data)

df.plot(x='Day', y='Sales', kind='line')
plt.title('Daily sales over a week')
plt.xlabel('Day of the week')
plt.ylabel('Sales in USD')
plt.show()
'''

data2 = {
    'Product': ['A', 'B', 'C', 'D'],
    'Rating': [4.2, 3.8, 4.5, 4.0]
}

df2 = pd.DataFrame(data2)
df2.plot(x='Product', y='Rating', kind='bar', color='green')
plt.title('Product Rating')
plt.xlabel('Product')
plt.ylabel('Average Rating')
plt.show()
