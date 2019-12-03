
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

from tensorflow.keras.layers import Dense, Flatten, Conv2D, BatchNormalization, MaxPooling2D
from tensorflow.keras import Model
import dataset_creator
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

class MyModel(Model):
  def __init__(self):
    super(MyModel, self).__init__()
    self.conv1 = Conv2D(32, 3)
    self.conv2 = Conv2D(64,32)

    self.maxPool = MaxPooling2D(2,2, padding='same')
    self.flatten = Flatten()
    
    self.bn1 = BatchNormalization()
    self.bn2 = BatchNormalization()

    self.d1 = Dense(128)
    self.bn3 = BatchNormalization()
    self.d2 = Dense(3)

  def call(self, x, is_train=False):
    #x = tf.reshape(x,[-1,100,100,3])
    x = self.conv1(x)
    x = self.maxPool(x)
    x = self.bn1(x, training=is_train)
    x = tf.nn.relu(x)
    x = self.conv2(x)
    x = self.maxPool(x)
    x = self.bn2(x, training = is_train)
    x = tf.nn.relu(x)
    x = self.flatten(x)
    x = self.d1(x)
    x = self.bn3(x, training=is_train)
    x = tf.nn.relu(x)
    return tf.nn.softmax(self.d2(x))
