#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : This function will gather and return the data to the user
class Load_Data():
    #Load Data
    def __init__():
        print('Load_Data is created')

	def load_data_from folder(self, path_list,name_list,test_size):
		for path in path_list:
			data = load_data(path,name_list, test_size)
			data_list.append(data)

		return data_list

    def load_data(self, path, name_list,test_size):
        df = pandas.read_csv(path, names = name_list)
        input = df[['center']].values
        output = df[['steering']].values
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=, random_state=)
        # random_state = int for random seed for splitting
        # test_size = proportion of data set to include in the test
        input_train,input_test, output_train, output_test = train_test_split(input, output,test_size = test_size,1)
        return [input_train, input_test, output_train, output_test]
