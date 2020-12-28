# -*- coding: utf-8 -*-
"""Book_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m3LLUY4e76IfwK1z1KMxLWxEHj4Vkfh3
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
# %matplotlib inline

!git clone 'https://github.com/sachinkavindaa/Machine-learning-with-Python'

df = pd.read_csv('/content/Machine-learning-with-Python/ML/Book/Book_1.csv')
df.head()

merged_1 = df[[	'raw_1','raw_2','raw_3','raw_4','raw_5','raw_6','raw_7','raw_8','raw_11(A2)']]
merged_1.head()

from sklearn.model_selection import train_test_split

X = merged_1.drop('raw_11(A2)',axis = 1).values
y = merged_1['raw_11(A2)'].values

X_train,X_test,y_train,y_test = train_test_split(X,y, random_state = 1)

X_train.shape

X_test.shape

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop

model = Sequential()

model.add(Dense(8, input_dim = 8,  activation = 'relu'))
keras.layers.Dropout(0.2)
model.add(Dense(3, activation = 'relu'))
keras.layers.Dropout(0.2)
model.add(Dense(3, activation = 'relu'))
#model.add(Dense(164, activation = 'relu'))
keras.layers.Dropout(0.2)
model.add(Dense(1, activation = 'sigmoid'))

model.compile(optimizer= 'adam', loss ='binary_crossentropy', )

model.fit(X_train,y_train,epochs=800)

loss_df = pd.DataFrame(model.history.history)

loss_df.plot()

model.evaluate(X_test,y_test)

model.evaluate(X_train,y_train)

pred = model.predict(X_test)

pred= pd.Series(pred.reshape(4,))

pred_df = pd.DataFrame(y_test,columns=['Test True Y'])

pred_df = pd.concat([pred_df,pred],axis = 1)

pred_df.columns = ['Test True Y','Model Prediction']
pred_df

y_test

sns.scatterplot(x = 'Test True Y', y = 'Model Prediction', data = pred_df)
plt.plot(y_test,y_test,'r')

from matplotlib import pyplot
pyplot.plot(pred, label='Model Prediction')
pyplot.plot(y_test, label='Test True Y')
pyplot.legend()
pyplot.show()

