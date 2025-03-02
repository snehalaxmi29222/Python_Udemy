import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = {
    'X':[1,2,3,4,5],
    'y': [2,4,6,8,10]
}

df = pd.DataFrame(data)

X= df[['X']]
y = df['y']

model = LinearRegression()
model.fit(X,y)

prediction = model.predict(X)
print(prediction)
print(model.coef_)
print(model.intercept_)