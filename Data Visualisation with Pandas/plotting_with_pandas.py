import pandas as pd
import matplotlib.pyplot as plt

'''data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Temperature': [22,21,19,24,23]
} 
df = pd.DataFrame(data)

df.plot(x='Day', y='Temperature', kind='line', title='Temperature trend over the week')
plt.show()
'''

'''data2 = {
    'Product': ['A','B','C','D'],
    'Sales': [150, 120, 200, 180]
}


df2 = pd.DataFrame(data2)

df2.plot(x='Product', y='Sales', kind='bar', title='Sales of Product', color='Orange')
plt.show()
'''

data3 = {
    'Age': [22,25,28,29,30,35,38,40]  
}

df3 = pd.DataFrame(data3)

df3.plot(kind='hist', bins=5, title='Customer Age Distribution')
plt.show()