# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xw9FEdLWctrZVBM0fKgbM8vkN7sm8Jdp
"""

from keras.layers import Dense
from keras.models import Sequential
import tensorflow as tf
tf.random.set_seed(1)

model = Sequential([
    Dense(1, input_shape=(1,), activation='linear')
])

model.get_weights()

import numpy as np

X = np.array([[1], [3], [2], [10], [4], [7], [8]])
y = np.array([[3, 9, 6, 30, 12, 21, 24]]).T

from keras.layers import Dense
from keras.models import Sequential

model = Sequential([
    Dense(1, input_shape=(1,), activation='linear')
])
model.summary()

w1, w0 = model.get_weights()
w1, w0

X[:1]

model.predict(X[:1])

"""w1 * x[:1] + w0  вес умножили на единицу и добавили сдвиг"""

from keras.activations import linear
linear(w1 * X[:1] + w0)

model.compile(optimizer='sgd', loss='mse', metrics='mae')

"""sgd - стохатический градиентый спуск, mse - функция потерь mse, mae - метрики которые хотим оптемизировать """

# Commented out IPython magic to ensure Python compatibility.
# %%time
# model.fit(X, y, epochs=100)

"""обучение модели: fit - обучение, передаем данные обучающие признаки и целевые значения, и количество обучений (любая сеть обучается на ошибках)"""

user_inp1, user_inp2 = 5, -9
print(f"Проверка на новых данных: {user_inp1} {user_inp2}")
print("Предсказание нейронной сети: ")
print(model.predict(np.array([[user_inp1], [user_inp2]])))

"""Берем 5 и -9, вызываем предикт."""

nw1, nw0 = model.get_weights()
print('w1 before', w1, 'w1 after', nw1)
print('w0 before', w0, 'w0 after', nw0)

"""После обучеия веса увеличились"""

import pandas as pd

pd.DataFrame({
   'true': np.squeeze(y),
   'pred': np.squeeze(model.predict(X))
})