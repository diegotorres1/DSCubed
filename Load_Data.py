#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : This function will gather and return the data to the user
import pandas as pd
from sklearn.model_selection import train_test_split
class Load_Data():
    #Load Data
    def __init__(self):
        print('Load_Data is created')



    def combine_contents(self,data, data_list):
        input_train_insert = data[0]
        input_test_insert = data[1]
        output_train_insert = data[2]
        output_test_insert = data[3]


        data_list[0] = data_list[0] + input_train_insert
        data_list[1] = data_list[1] + input_test_insert
        data_list[2] = data_list[2] + output_train_insert
        data_list[3] = data_list[3] + output_test_insert

        return data_list

    def load_data_from_folder(self, path_list,name_list,test_size):
        for path in path_list:
            data = self.load_data(path,name_list, test_size)
            self.combine_contents(data, data_list)
            # data_list.append(data)

        return data_list

    def load_data(self, path, name_list,test_size):
        df = pd.read_csv(path, names = name_list,engine='python')
        input = df[['center']].values
        output = df[['steering']].values
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=, random_state=)
        # random_state = int for random seed for splitting
        # test_size = proportion of data set to include in the test
        input_train,input_test, output_train, output_test = train_test_split(input, output,test_size = test_size,random_state = 1)
        return [input_train, input_test, output_train, output_test]
