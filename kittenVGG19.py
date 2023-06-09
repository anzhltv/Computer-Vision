# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A5CDIAXxBziZlz-pwbes9ycDvU5E9uL5
"""

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from tensorflow import keras
from google.colab import files
from io import BytesIO
from PIL import Image
from keras.preprocessing import image as kp_image

model = keras.applications.VGG19()

upload = files.upload()

img = Image.open(BytesIO(upload['imgonline-com-ua-Resize-Ze5bEW6pljOjxJ.jpg']))
plt.imshow(img)

img = np.array(img)
x = keras.applications.vgg16.preprocess_input(img)
print(x.shape)
x = np.expand_dims(x, axis=0)
print(x.shape)

res = model.predict( x )
print(np.argmax(res))

""" 284: 'Siamese cat, Siamese',"""