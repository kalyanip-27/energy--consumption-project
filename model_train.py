import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("dataset/energy_data.csv")

X = data[['Temperature','Humidity','Appliances']]
y = data['Energy']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)

pickle.dump(model, open("model/model.pkl","wb"))

print("Model trained successfully")