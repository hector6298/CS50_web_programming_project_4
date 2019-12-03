
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

from tensorflow.keras.layers import Dense, Flatten, Conv2D, BatchNormalization, MaxPooling2D
from tensorflow.keras import Model
import dataset_creator
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from neuralNetModel import MyModel
from dataset_creator import Image
import time

diagnostic = {
    0 : 'melanoma',
    1 : 'atypical nevu',
    2 : 'common nevu'
}

IMG_PATH = "img/"

image = Image('IMD437', IMG_PATH)

model = MyModel()
model.load_weights('./checkpoints/checkpoint')
img = image.img
img = np.reshape(img, [1,100,100,3])

print(img.shape)
start = time.time()
prediction = model(img, False)

diag = diagnostic[np.argmax(prediction.numpy())]
print(diag)
print(time.time() - start)