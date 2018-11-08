from Load_Data import Load_Data
def main():
    ld = Load_Data()
    name_list = ['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed']
    path = 'D:\\UCI\\Senior Design Project\\Training Data\\driving_log.csv'

    #Need to change the path when I run it on the machine
    path_list = [
    		'D:\\UCI\\Senior Design Project\\Training Data\\driving_log.csv',
    		'D:\\UCI\\Senior Design Project\\Training Data Set 2\\driving_log.csv',
    		'D:\\UCI\\Senior Design Project\Training Data Set 3\\driving_log.csv'
    ]


    test_size = .1
    data = ld.load_data(path, name_list,test_size)
    print('Data Type:\t' + str(type(data)))
    print('Data:\t' + str(len(data[0])))
    print('\t' + str(data[2]))
    # data_list = ld.load_data_from_folder(path_list,name_list,test_size)
    # print('Data Type:\t' + str(type(data)))
    # print('Data:\t' + str(len(data[0])))


if __name__ == '__main__':
	main()
	print('Test Load Data')
