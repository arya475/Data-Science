
import numpy as np
from numpy import random  
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
import os
from sklearn.model_selection import train_test_split
import joblib

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'heart_model.pkl')
model_main = joblib.load(model_path)

umur = pd.DataFrame(random.randint(20, 80, size=10000), columns=['age'])
sex = pd.DataFrame(random.randint(0,2, size=10000), columns=['sex'])
cp = pd.DataFrame(random.randint(0,4, size=10000), columns=['cp'])
tensi = pd.DataFrame(random.randint(90, 200, size=10000), columns=['trestbps'])
chol = pd.DataFrame(random.randint(150,340, size=10000), columns=['chol'])
fbs = pd.DataFrame(random.randint(0, 2, size=10000), columns=['fbs'])
restecg = pd.DataFrame(random.randint(0, 3, size=10000), columns=['restecg'])
talach = pd.DataFrame(random.randint(80, 220, size=10000), columns=['thalach'])
exang = pd.DataFrame(random.randint(0, 2, size=10000), columns=['exang'])
oldpeak = pd.DataFrame(random.choice([0.1,0.2,0.3,0.4,0.5,1,1.5,1.3,1.8,2.1,2.3,2.6,3.2,3.5,4.8,4.5,4.2],size=10000), columns=['oldpeak'])
slope = pd.DataFrame(random.randint(0, 3, size=10000), columns=['slope'])
ca = pd.DataFrame(random.randint(0, 4, size=10000), columns=['ca'])
thal = pd.DataFrame(random.randint(0, 4, size=10000), columns=['thal'])

data = pd.concat([umur, sex, cp, tensi,chol, fbs, restecg, talach, exang, oldpeak,slope,ca,thal], axis=1)
print(data.head())

prediksi = model_main.predict(data)
print(prediksi)

data.loc[:, 'target'] = prediksi
print(data.head(20))


# Membuatkan data csv baru
data.to_csv('heart10k.csv')



