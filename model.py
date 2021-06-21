import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data=pd.read_csv("dataset.csv")
x=data['YearsExperience'].values.reshape(-1,1)
y=data['Salary'].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

reg=LinearRegression()
reg.fit(x_train,y_train)
pickle.dump(reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))