#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : This function will return sequential model
import pandas as pd # data analysis toolkit - create, read, update, delete datasets
import numpy as np #matrix math
from sklearn.model_selection import train_test_split #to split out training and testing data
#keras is a high level wrapper on top of tensorflow (machine learning library)
#The Sequential container is a linear stack of layers
from keras.models import Sequential
#popular optimization strategy that uses gradient descent
from keras.optimizers import Adam
#to save our model periodically as checkpoints for loading later
from keras.callbacks import ModelCheckpoint
#what types of layers do we want our model to have?
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
#helper class to define input shape and generate training images given image paths & steering angles
from utils import INPUT_SHAPE, batch_generator
#for command line arguments
import argparse
#for reading files
import os
class Create_Model():
    def __init__(self):
        print('Create_Model is created')
    def create_model(self,keep_prob):
        #Models in Keras can come in two forms Sequential and Functional API
        #The functional API is for building more complicated NNs
        #Define the Model Architecture
        #######################################################################
        model = Sequential()
        #lambda layers are used to define custom layers
        model.add(Lambda(lambda x : (x/127.5) - 1.0, input_shape = INPUT_SHAPE))
        #######################################################################

        #Convolutional Kernel applied to the input layer
        #filter - dimension of the output space
        #kernel size - dimension of the kernel
        #strides - the strides of the kernel along the input
        #subsample - reduce complexity by picking unique elements in matrix

        #The default step size if (1,1)
        #avoid saturation
        #Conv Layers are meant to handle feature engineering

        #######################################################################
        model.add(Conv2D(24,5,5,activation = 'relu',subsample=(2,2)))
        model.add(Conv2D(36, 5, 5, activation='relu', subsample=(2, 2)))
        model.add(Conv2D(48, 5, 5, activation='relu', subsample=(2, 2)))

        model.add(Conv2D(64, 3, 3, activation='relu'))
        model.add(Conv2D(64, 3, 3, activation='relu'))
        #######################################################################

        #Percentage of the input weights that are kept
        #Typically want to use the between 20% and 50%
        #Used to prevent over fitting
        #######################################################################
        model.add(Dropout(keep_prob))
        model.add(Dropout(keep_prob))
        #######################################################################
        #Fully connected layers
        #Flatten the layer to a 1D vector so they can be passed to the dense layers
        #Slowly decrease the output size of each layer of nodes
        #We want the last dense layer to be the number of classes
        #rrelu activation function is a good place to start
        #######################################################################
        model.add(Flatten())
        model.add(Dense(100,activation = 'relu'))
        model.add(Dense(50,activation = 'relu'))
        model.add(Dense(10,activation = 'relu'))
        model.add(Dense(1))
        #######################################################################

        #print a model summary
        #shows the output shape and the param length
        model.summary()
        return model





		#Additional Notes#
		#Max Pooling is a way to reduce the number of parameters by sliding a filter across
