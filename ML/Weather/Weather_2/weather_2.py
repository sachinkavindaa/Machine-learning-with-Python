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

df = pd.read_csv('/content/Machine-learning-with-Python/ML/Weather/Weather.csv')
df.head()

merged = df[['T Max', 'T Min', 'Wind', 'Could','Precip','Humidity','Pressure']]
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
X_train,X_test,y_train,y_test = train_test_split(df_scaled[['T Max', 'T Min', 'Wind', 'Could','Humidity','Pressure']],merged.Precip,test_size =0.2,random_state=25)

X_train

df_scaled.shape

len(X_train)

X_train_scaled = X_train.copy()
X_train_scaled[['T Max', 'T Min', 'Wind', 'Could','Humidity','Pressure']]= X_train_scaled[['T Max', 'T Min', 'Wind', 'Could','Humidity','Pressure']]

X_test_scaled = X_test.copy()
X_test_scaled[['T Max', 'T Min', 'Wind', 'Could','Humidity','Pressure']]= X_test_scaled[['T Max', 'T Min', 'Wind', 'Could','Humidity','Pressure']]

X_train_scaled

model = keras.Sequential([
                          keras.layers.Dense(1,input_shape=(6,),activation='sigmoid',kernel_initializer='ones',bias_initializer='zeros')
])

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(X_train_scaled,y_train,epochs=10000)

X_test_scaled

model.predict(X_test_scaled)

y_test

coef, intercept = model.get_weights()
coef, intercept

def sigmoid(x):
  import math
  return 1/(1+math.exp(-x))
sigmoid(18)

