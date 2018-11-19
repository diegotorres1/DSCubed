#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : train_steer handles the calling the main processes for training
	#the steering. The main processes that it calls are
		#Loading the Data from the CSV files
		#Creating the model
		#Then training the model on the data that was loaded
from Train_Model import Train_Model
from Load_Data import Load_Data
from Create_Model import Create_Model
from GPU_Checker import GPU_Checker
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
def main():
    parser = argparse.ArgumentParser(description = 'Process Training Params')
    parser.add_argument('-tp', help='training parameters',dest='training_parameters',type=str, default='param')
    parser.add_argument('-dd', help='data directory',dest='data_dir',type=str,default='data')
    args = parser.parse_args()

    #Show inputs
    print('Inputs: ')
    for key, value in vars(args).items():
        print('%s : %s' % (str(key), str(value)))
    print('=' * 10)

    #Training Configuration File Load
    df = pd.read_csv(args.training_parameters, encoding = 'utf-8')
    print(df.to_string())
    if(df['save_best_only'][0] ==  'TRUE'):
    	df['save_best_only'][0] = True
    else:
    	df['save_best_only'][0] = False

    #Create helper objects
    ld = Load_Data()
    tm = Train_Model()
    cm = Create_Model()
    ###########################################################################
    #Load Data
    name_list=['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed']
    print('Load Data from ...')
    path_list = []
    folder_list = os.listdir(args.data_dir)
    for f in folder_list:
        if(f.find('Training Data') >= 0):
            path_list.append(args.data_dir + '/' + f + '/driving_log.csv')
            print('\t'+args.data_dir + '/' + f)

    print('=' * 10)
    #Paths to the CSV files
    # path_list = [
    # 		'D:\\UCI\\Senior Design Project\\Training Data\\driving_log.csv',
    # 		'D:\\UCI\\Senior Design Project\\Training Data Set 2\\driving_log.csv',
    # 		'D:\\UCI\\Senior Design Project\Training Data Set 3\\driving_log.csv'
    # ]
    data = ld.load_data_from_folder(path_list, name_list,df['test_size'][0])
    ###########################################################################
    #Create Model
    print('Creating the model ... ')
    model = cm.create_model(df['keep_prob'][0])
    ###########################################################################
    #Train Model
    print('Begin training the model ...')
    print(df['checkpoint_path'][0])
    tm.train_model(df['checkpoint_path'][0],model,df,data,args.data_dir)



if __name__ == '__main__':
	main()
	print('Train Steering Complete')
	print('Libraries used :')
	print('\t--Keras')
	print('\t--Numpy')
	print('\t--Pandas')
