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
from GPU_Checker import CPU GPU_Checker
import argparse
def main():
	parser = argparse.ArgumentParser(description = 'Process Training Params')
	parser.add_argument('-l', help = 'learning rate', type = float)
	parser.add_argument()

	ld = Load_Data()
	tm = Train_Model()
	cm = Create_Model()

	#Load Data

	#Paths to the CSV files
	path_list = [
			'D:\\UCI\\Senior Design Project\\Training Data\\driving_log.csv',
			'D:\\UCI\\Senior Design Project\\Training Data Set 2\\driving_log.csv',
			'D:\\UCI\\Senior Design Project\Training Data Set 3\\driving_log.csv'
	]

	ld.load_data_from(path_list, )



if __name__ == '__main__':
	main()
	print('Train Steering Complete')
	print('Libraries used :')
	print('\t--Keras')
	print('\t--Numpy')
	print('\t--Pandas')
