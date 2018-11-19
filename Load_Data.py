#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : This function will gather and return the data to the user
import pandas as pd
import numpy as np
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
        print(input_train_insert[0])
        print(len(input_train_insert))
        print(data_list[0])
        # print(input_test_insert[1])
        print(type(data_list[0]))
        print(type(input_test_insert))

        # data_list[0] = data_list[0] + input_train_insert
        # data_list[1] = data_list[1] + input_test_insert
        # data_list[2] = data_list[2] + output_train_inser
        # data_list[3] = data_list[3] + output_test_insert

        data_list[0] = np.concatenate((data_list[0], input_train_insert), axis=0)
        data_list[1] = np.concatenate((data_list[1], input_test_insert), axis=0)
        data_list[2] = np.concatenate((data_list[2], output_train_insert), axis=0)
        data_list[3] = np.concatenate((data_list[3], output_test_insert), axis=0)


        return data_list

    def load_data_from_folder(self, path_list,name_list,test_size):
        # names=['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed']
        count = 0
        data_list = []
        for path in path_list:
            data = self.load_data(path,name_list, test_size)
            if(count == 0):
                data_list = data.copy()
            else:
                self.combine_contents(data, data_list)
            count += 1
            # data_list.append(data)

        return data_list

    def load_data(self, path, name_list,test_size):
        df = pd.read_csv(path, names = name_list,engine='python')
        print(list(df.columns.values))
        input = df[['center','left','right']].values
        output = df[['steering']].values
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=, random_state=)
        # random_state = int for random seed for splitting
        # test_size = proportion of data set to include in the test
        input_train,input_test, output_train, output_test = train_test_split(input, output,test_size = test_size,random_state = 1)
        return [input_train, input_test, output_train, output_test]
