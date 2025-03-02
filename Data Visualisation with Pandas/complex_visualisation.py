import pandas as pd
import matplotlib.pyplot as plt

'''data = {
    'Age': [22,25,28,30,32,35,39,40,44,50,55,60,65,70]
}

df = pd.DataFrame(data)

df.plot(kind='hist', bins=7, edgecolor='black', title='Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
'''
'''data2 = {
    'Height': [150, 160, 165, 170],
    'Weight': [50, 60, 70, 75]
}

df2 = pd.DataFrame(data2)

df2.plot(kind='scatter', x='Height', y='Weight', title='Height vs Weight', color='red')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

plt.show()
'''

data3 = {
    'Exam Score': [75, 80, 85, 90, 95, 99]
    
}
df3 = pd.DataFrame(data3)
df3.plot(kind='box', title='Distribution of Exam Score', vert=False)
plt.xlabel('Exam Score')
plt.show()

