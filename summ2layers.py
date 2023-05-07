# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ioxLlkJV4bAt8hF2SFz9IVrTiCEz3nKS
"""

import numpy as np
X1 = np.random.randint(1, 10, size=50)
X2 = np.random.randint(1, 10, size=50)

y = X1 + X2

X = np.vstack([X1,X2]).T
X

y = y[None]
y = y.T
y

"""Т.к. сети - это куча маленьких линейных регрессий, а им нужно масштабирование данных, то и для нейросетей, так же нужно масштабирование данных.

Если что поизучать StandardScaler и MinMaxScaler можно в этом видео


"""

from sklearn.preprocessing import MinMaxScaler

mms = MinMaxScaler()
X_norm = mms.fit_transform(X)

X_norm

"""Это нужно для облегчения обучения """

from keras.layers import Dense
from keras.models import Sequential
import tensorflow as tf
tf.random.set_seed(9)

model = Sequential([
    Dense(3, input_shape=(2,), activation='linear'),
    Dense(1, activation='linear')
])

model.summary()

model.get_weights()

model.compile(optimizer='sgd', loss='mse', metrics='mae')

# Commented out IPython magic to ensure Python compatibility.
# %%time 
# model.fit(X_norm, y, epochs=200)

test_X = [[4, 2],
          [6, 2], [9, 1]]
test_X = mms.transform(test_X)
print("Предсказание нейронной сети: ")
print(model.predict(np.array(test_X)))

import pandas as pd

pd.DataFrame({
    'x1': X[:, 0],
    'x2': X[:, 1],
    'true': np.squeeze(y),
    'pred': np.squeeze(model.predict(X_norm))
}).head(10)