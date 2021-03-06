# -*- coding: utf-8 -*-
"""Weather_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GC-Y0DyMAzszHo0svwqMs0tugz08n8uS

# Weather Forecast

Here considering given data set, compiled over the 10000 epochs finally able to get description of the data set.

loss: -7.5724 

accuracy: 0.0993
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
from sklearn import preprocessing
# %matplotlib inline

!git clone 'https://github.com/sachinkavindaa/Machine-learning-with-Python'

df = pd.read_csv('/content/Machine-learning-with-Python/ML/Weather/Weather_3/Weather.csv')
df.head()

merged = df[['T_Max', 'T_Min', 'Wind', 'Could','Precip','Humidity','Pressure']]
merged.head()

def min_max_scaling(merged):
    # copy the dataframe
    df_norm = merged.copy()
    # apply min-max scaling
    for column in df_norm.columns:
        df_norm[column] = (df_norm[column] - df_norm[column].min()) / (df_norm[column].max() - df_norm[column].min())
        
    return df_norm
    
# call the min_max_scaling function
df_scaled = min_max_scaling(merged)

df_scaled

df_scaled.info()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df_scaled[['T_Max', 'T_Min', 'Wind', 'Could','Humidity','Pressure']],df_scaled.Precip,test_size =0.2,random_state=25)

X_train

df_scaled.shape

len(X_train)

X_train_scaled = X_train.copy()
X_train_scaled[['T_Max', 'T_Min', 'Wind', 'Could','Humidity','Pressure']]= X_train_scaled[['T_Max', 'T_Min', 'Wind', 'Could','Humidity','Pressure']]

X_test_scaled = X_test.copy()
X_test_scaled[['T_Max', 'T_Min', 'Wind', 'Could','Humidity','Pressure']]= X_test_scaled[['T_Max', 'T_Min', 'Wind', 'Could','Humidity','Pressure']]

X_train_scaled

model = keras.Sequential([
                          keras.layers.Dense(1,input_shape=(6,),activation='sigmoid',kernel_initializer='ones',bias_initializer='zeros')
])

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(X_train_scaled,y_train,epochs=300)

X_test_scaled

model.evaluate(X_test_scaled,y_test)

model.predict(X_test_scaled)

y_test

coef, intercept = model.get_weights()
coef, intercept

def sigmoid(x):
  import math
  return 1/(1+math.exp(-x))
sigmoid(8)

X_test

def prediction_function(T_max,T_min,Wind,Could,Pressure,Humidity):
  weighted_sum = coef[0] * T_max + coef[1] * T_min + coef[2] * Wind + coef[3] * Could + coef[4] * Pressure + coef[5] * Humidity + intercept
  return sigmoid(weighted_sum)

prediction_function(0.88, 0.008850 , 0.047619 , 0.170213 ,0.607143,	0.995619)

"""When we input the variable values of the corresponding to the 364 raw, we can get value 0.40268136412389227. 



model.predict(X_test_scaled) line gives the same value relative to 364 raw array in 0.40268135.
"""