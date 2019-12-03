import cv2
import tensorflow as tf
import numpy as np
import os
import pandas as pd
from sklearn.model_selection import train_test_split


class Image(object):

    def __init__(self,img_tag,imgs_path):
        self.img_tag = img_tag
        img = cv2.imread(imgs_path+self.img_tag+'.bmp')
        img = cv2.resize(img, (100,100))
        self.img = np.resize(img, img.shape[0]*img.shape[1]*img.shape[2]).astype(np.float32)



def make_data_matrix(csv_file):
    IMG_PATH = "img/"
    train_imgs = []
    tags, labels = extract_tags_n_labels(csv_file)
    for tag in tags:
        image = Image(tag, IMG_PATH)
        train_imgs.append(image.img)
    train_imgs = np.array(train_imgs)
    print('imgs'+str(train_imgs.shape))
    x_train, x_text, y_train, y_test = train_test_split(train_imgs, labels, test_size=0.15, random_state=42)
    return x_train, x_text, y_train, y_test

def extract_tags_n_labels(file):
    dataframe = pd.read_csv(file)
    labels = dataframe.iloc[:,1:4]
    labels = labels.to_numpy()
    tags = dataframe.iloc[:,0]
    print('labels'+str(labels.shape))
    tags = tags.to_numpy()
    return tags, labels


def input_fn(data, labels, batch_size, is_train):
    dataset = tf.data.Dataset.from_tensor_slices((data,labels))
    if(is_train):
        dataset = dataset.shuffle(10000)
        dataset = dataset.repeat()
    dataset = dataset.batch(batch_size)
    return dataset
