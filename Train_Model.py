#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : This function will gather and return the data to the user
class Train_Model():
	def __init__():
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


	def train_model(self,checkpoint_file_path,model, model_param_dict,data):

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
			filepath = checkpoint_file_path,
			monitor = 'value_loss',
			verbose = 1,
			save_best_only = True,
			mode = 'min'
		)
		#######################################################################


		#generator makes batches of samples
		#the batch samples are configured by the number of epochs and the batch sizes
        #Need to define features, labels, batch_size
		model.fit_generator(
			generator(
				model_param_dict['features'][0],
				model_param_dict['labels'][0],
				model_param_dict['batch_size'][0]
			),
			samples_per_epoch = model_param_dict['samples_per_epoch'][0],
			nb_epoch = model_param_dict['number_epoch'][0],
			verbose = 1,
			callbacks = [checkpoint]
		)
		#compiling enables the training to begin
		#the model will be trained based on the batches created by the fit generator
