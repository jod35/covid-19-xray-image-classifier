import os
import numpy as np
import random
import cv2



# Deep learning libraries
import keras.backend as K
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, SeparableConv2D, MaxPool2D, LeakyReLU, Activation
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import tensorflow as tf

from sklearn.metrics import accuracy_score, confusion_matrix

#For graphical confusion metric
import matplotlib.pyplot as plt
import seaborn as sns

img_dims = 150
batch_size=32

BASE_DIR=os.path.dirname(os.path.realpath(__file__))


DIAGNOSIS_MESSAGES = [ "Pneumonia detected", "Covid19 detected", "Normal lungs detected" ]
def defineModelArchitecture (_img_dims ):
    # Input layer
    inputs = Input(shape=(_img_dims, _img_dims, 3))

    # First conv block
    x = Conv2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same')(inputs)
    x = Conv2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    # Second conv block
    x = SeparableConv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = SeparableConv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    # Third conv block
    x = SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    # Fourth conv block
    x = SeparableConv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = SeparableConv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)
    x = Dropout(rate=0.2)(x)

    # Fifth conv block
    x = SeparableConv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = SeparableConv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)
    x = Dropout(rate=0.2)(x)

    # FC layer
    x = Flatten()(x)
    x = Dense(units=512, activation='relu')(x)
    x = Dropout(rate=0.7)(x)
    x = Dense(units=128, activation='relu')(x)
    x = Dropout(rate=0.5)(x)
    x = Dense(units=64, activation='relu')(x)
    x = Dropout(rate=0.3)(x)

    # Output layer
    output = Dense(units=1, activation='sigmoid')(x)

    return inputs, output

def process_data(___inputPath, img_dims, batch_size):
    # Data generation objects
    train_datagen = ImageDataGenerator(rescale=1./255, zoom_range=0.3, vertical_flip=True)
    test_val_datagen = ImageDataGenerator(rescale=1./255)

    # This is fed to the network in the specified batch sizes and image dimensions
    train_gen = train_datagen.flow_from_directory(
    directory=___inputPath+'train',
    target_size=(img_dims, img_dims),
    batch_size=batch_size,
    class_mode='binary',
    shuffle=True)

    test_gen = test_val_datagen.flow_from_directory(
    directory=___inputPath+'test',
    target_size=(img_dims, img_dims),
    batch_size=batch_size,
    class_mode='binary',
    shuffle=True)

    # I will be making predictions off of the test set in one batch size
    # This is useful to be able to get the confusion matrix
    test_data = []
    test_labels = []

    for cond in ['/NORMAL/', '/PNEUMONIA/']:
        for img in (os.listdir(___inputPath + 'test' + cond)):
            img = cv2.imread(___inputPath+'test'+cond+img,0) #Replace plt.imread, with  gray scale cv2.imread(path,0), so that ui's image load process doesn't throw a pyimage10 error
            img = cv2.resize(img, (img_dims, img_dims))
            img = np.dstack([img, img, img])
            img = img.astype('float32') / 255
            if cond=='/NORMAL/':
                label = 0
            elif cond=='/PNEUMONIA/':
                label = 1
            test_data.append(img)
            test_labels.append(label)

    test_data = np.array(test_data)
    test_labels = np.array(test_labels)

    return train_gen, test_gen, test_data, test_labels


def reportFileDistributions (___inputPath, directoryProcessArray ):
    for _set in directoryProcessArray:
        n_normal = len(os.listdir(___inputPath + _set + '/NORMAL'))
        n_infect = len(os.listdir(___inputPath + _set + '/PNEUMONIA'))
        print('Set: {}, normal images: {}, illness-positive images: {}'.format(_set, n_normal, n_infect))



seed = 232
np.random.seed(seed)
tf.random.set_seed(seed)



########################################################################
#SECTION A: MODEL ARCHITECTURE NON-COVID19 PNEUMONIA DETECTOR

inputs, output = defineModelArchitecture ( img_dims )

# Creating model and compiling
model_pneumoniaDetector = Model(inputs=inputs, outputs=output)
model_pneumoniaDetector.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_pneumoniaDetector.load_weights(os.path.join(BASE_DIR,'best_weights.hdf5'))

########################################################################
#SECTION B: NON-COVID19  PNEUMONIA VS NORMAL LUNG ACCURACY REPORT [LOADED MODEL/WEIGHTS]
print('\n\n#######TRAINED NON-COVID19 PNEUMONIA VS NORMAL LUNG TEST REPORT [LOADED MODEL/WEIGHTS]')
# Lets first look at some of our X-ray images and how each dataset is distributed:

input_path_b = os.path.join(BASE_DIR,'xray_dataset/')

# Report file distributions
reportFileDistributions (input_path_b, ['train', 'val', 'test'] )

# Getting the data
train_gen, test_gen, test_data_b, test_labels_b = process_data(input_path_b, img_dims, batch_size)

# Reporting on accuracies
#renderConfusionMetrics ( model_pneumoniaDetector, test_data_b, test_labels_b, False, None, None, None, None, None )



########################################################################
#SECTION C: MODEL ARCHITECTURE COVID19 DETECTOR

inputs, output = defineModelArchitecture ( img_dims )


# Creating model and compiling
model_covid19PneumoniaDetector = Model(inputs=inputs, outputs=output)
model_covid19PneumoniaDetector.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_covid19PneumoniaDetector.load_weights(os.path.join(BASE_DIR,'covid19_neural_network_weights_jordan.hdf5'))


###################################################################
#SECTION D: COVID19 PNEUMONIA VS NORMAL LUNG ACCURACY REPORT [LOADED MODEL/WEIGHTS]
print('\n\n#######TRAINED COVID19 PNEUMONIA VS NORMAL LUNG TEST REPORT [LOADED MODEL/WEIGHTS]')
      
#Jordan_note establish custom_path for covid 19 test data
input_path_d = os.path.join(BASE_DIR,'xray_dataset_covid19/')


# Report file distributions
reportFileDistributions (input_path_d, ['train', 'test'])

# Getting the data
train_gen_d, test_gen_d, test_data_d, test_labels_d = process_data(input_path_d, img_dims, batch_size)

# Reporting on accuracies
#renderConfusionMetrics ( model_covid19PneumoniaDetector, test_data_d, test_labels_d, False, train_gen_d, test_gen_d, batch_size, 11, 'covid19_neural_network_weights_jordan_v2.hdf5' )



model_pneumoniaDetector = model_pneumoniaDetector
model_covid19PneumoniaDetector = model_covid19PneumoniaDetector


# model_covid19PneumoniaDetector.sa

import datetime
def recordInferenceEvent ( imagePath, outputContent ):
    currentDate = datetime.datetime.now()
    with open("inference_record.txt", "a") as text_file:
        text_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        text_file.write("DATE/TIME : " + str(currentDate.month) + " " + str(currentDate.day) + ", " + str(currentDate.year) + "..." + str(currentDate.hour) + ":" + str(currentDate.minute) + ":" + str(currentDate.second) + "\n\n") 
        text_file.write("IMAGE : " + imagePath + "\n\n")
        text_file.write("RESULT : \n" + outputContent + "\n\n\n\n")

def doOnlineInference_regularPneumonia (imagePath):
    test_data = []
    img = cv2.imread(imagePath,0) #Replace plt.imread, with  gray scale cv2.imread(path,0), so that ui's image load process doesn't throw a pyimage10 error
    img = cv2.resize(img, (img_dims, img_dims))
    img = np.dstack([img, img, img])
    img = img.astype('float32') / 255
    test_data.append(img)
    prediction = model_pneumoniaDetector.predict(np.array(test_data))
    _prediction = round( prediction[0][0]*100, 3 )
    if ( _prediction > 50 ):
        _prediction = DIAGNOSIS_MESSAGES[0];
    elif ( _prediction < 50 ):
        _prediction = DIAGNOSIS_MESSAGES[2];
    outputContent = _prediction + "\n"
    outputContent += "Raw Neural Network Output : \n" + str(prediction[0][0]) + ". A value closer to 1 signifies illness, while a value closer to 0 signifies normalness.\n\n"
    recordInferenceEvent (imagePath, outputContent)
    return outputContent


#Function written by Jordan to do online inference i.e. Covid19 tests
def doOnlineInference_covid19Pneumonia (imagePath):
    test_data = []
    img = cv2.imread(imagePath,0) #Replace plt.imread, with  gray scale cv2.imread(path,0), so that ui's image load process doesn't throw a pyimage10 error
    img = cv2.resize(img, (img_dims, img_dims))
    img = np.dstack([img, img, img])
    img = img.astype('float32') / 255
    test_data.append(img)
    prediction = model_covid19PneumoniaDetector.predict(np.array(test_data))
    _prediction = round( prediction[0][0]*100, 3 )
    if ( _prediction > 50 ):
        _prediction = DIAGNOSIS_MESSAGES[1];
    elif ( _prediction < 50 ):
        _prediction = DIAGNOSIS_MESSAGES[2];
    outputContent = _prediction + "\n"
    outputContent += "Raw Neural Network Output \n: " + str(prediction[0][0]) + ". A value closer to 1 signifies illness, while a value closer to 0 signifies normalness.\n\n"
    recordInferenceEvent (imagePath, outputContent)
    return outputContent

import sys
from PIL import Image, ImageTk

import os
import codecs



import cv2

CONSTANT_DIAGNOSIS_IMAGE_SPAN = 480

DIAGNOSIS_RESULT = ""
DIAGNOSIS_RESULT_FIELD = None
#Jordan_note: Added to facilitate output window data




def loadRegularPneumoniaImageFromName(filename):

    load = Image.open(filename)
    load = load.resize((CONSTANT_DIAGNOSIS_IMAGE_SPAN, CONSTANT_DIAGNOSIS_IMAGE_SPAN),Image.ANTIALIAS) #Resized "load" image to constant size on screen. However, neural network still runs on on original image scale from filename.


    DIAGNOSIS_RESULT=doOnlineInference_regularPneumonia (filename)

    data={
        "data":DIAGNOSIS_RESULT
    }
    
    return data





def loadCovid19ImageFromName(filename):

    load = Image.open(filename)
    load = load.resize((CONSTANT_DIAGNOSIS_IMAGE_SPAN, CONSTANT_DIAGNOSIS_IMAGE_SPAN),Image.ANTIALIAS) #Resized "load" image to constant size on screen. However, neural network still runs on on original image scale from filename.

    DIAGNOSIS_RESULT = doOnlineInference_covid19Pneumonia (filename)
    
    data={
        "data":DIAGNOSIS_RESULT
    }
    
    return data

