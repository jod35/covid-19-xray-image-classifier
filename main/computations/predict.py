
from keras.models import load_model
from keras.preprocessing.image import img_to_array,load_img
import tensorflow as tf
import numpy as np


network=load_model('./covid-19-model-5eps')


def convert_to_array(image_path):

    """
        Read the image and convert it into an array
    """
    img=load_img(image_path,target_size=(224,224))

    img_array=img_to_array(img)

    """Expand the dimensions"""

    img_array=tf.expand_dims(img_array,0)

    return img_array


def predict_image_class(image_array):
    predictions=network.predict(image_array,steps=1)

    score=tf.nn.softmax(predictions[0])

    class_names = ['covid','normal']

    final_class=class_names[np.argmax(predictions)]

    data={
        "score":score,
        "class":final_class
    }


    return data


