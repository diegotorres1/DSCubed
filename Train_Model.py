#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : This function will gather and return the data to the user
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
class Train_Model():
	def __init__(self):
		print('Train_Model is created')

	#generator
	def generator(self,features, labels, batch_size):
		'''
		generator - creates training data on a batch basis
		'''
		batch_features = np.zeros((batch_size, 64,64, 3))
		batch_labels = np.zeroes((batch_size, 1))

		while(True):
			for i in range(batch_size):
				index = random().choice(len(features), 1)
				batch_features[i] = some_processing(features[index])
				batch_labels[i] = labels[index]

		#yield returns an iterable which means that values are generated on the spot
		yield batch_features, batch_labels


	def train_model(self,checkpoint_file_path,model, model_param_dict,data,data_dir):

		#the optimizer is what changes the weights and biases during training
		#loss is the function to calculate the error
		#######################################################################
		model.compile(
			optimizer = Adam(model_param_dict['learning_rate'][0]),\
			loss = 'mean_squared_error',\
			metrics = ['accuracy']
		)
		#######################################################################
		#save model and continue the training for later
		#these are essentially the weights of the model
		#we want to save only when there is an improvement in accuracy of the model
		#monitor looks at the value loss
		#verbose shows more output in the terminal
		#save best only saves if the best
		#mode matches value loss
		#######################################################################
		checkpoint = ModelCheckpoint(
			filepath = checkpoint_file_path + 'model-{epoch:03d}.h5',
			monitor = 'value_loss',
			verbose = 1,
			save_best_only = True,
			mode = 'min'
		)
		#######################################################################


		#generator makes batches of samples
		#the batch samples are configured by the number of epochs and the batch sizes
        #Need to define features, labels, batch_size

        			#batch_generator(
        			#	model_param_dict['features'][0],
        			#	model_param_dict['labels'][0],
        			#	model_param_dict['batch_size'][0]
        			#),

		model.fit_generator(
            batch_generator(data_dir,data[0],data[2],model_param_dict['batch_size'][0],True)
            ,
			samples_per_epoch = model_param_dict['samples_per_epoch'][0],
			nb_epoch = model_param_dict['nb_epoch'][0],
            validation_data=batch_generator(data_dir, data[1], data[3], model_param_dict['batch_size'][0], False),
            nb_val_samples=len(data[1]),#input_test [input_train, input_test, output_train, output_test]
			verbose = 1,
			callbacks = [checkpoint]
		)
		#compiling enables the training to begin
		#the model will be trained based on the batches created by the fit generator
