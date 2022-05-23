import numpy as np
import csv

def read_data(file_name):
    # path = 'E:/Telemdycyna_projekt/'
    path = ''

    with open(path + file_name)as file:
        reader=csv.reader(file, delimiter=';')
        header = next(reader) #skipping header
        data = []
        for row in reader:
            data.append(row)
    file.close()
    data = np.array(data)
    return data

def replace_comma_with_dot(data):
    replaced_data = np.zeros(np.shape(data))
    for row in range(0,np.shape(data)[0]):
        for col in range(0,np.shape(data)[1]):
            replaced_data[row,col] = (data[row,col]).replace(',', '.')
    return replaced_data


