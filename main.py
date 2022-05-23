from functionalities import read_data, replace_comma_with_dot
from preprocessing import magnituda, filtering, find_peak, moving_variance, cut_non_gait_data
import numpy as np
import matplotlib.pyplot as plt

# Ręka - Laura
filename_1 = "acc_data_reka_1.csv"
filename_2 = "acc_data_reka_2.csv"
filename_3 = "acc_data_reka_3.csv"
filename_4 = "acc_data_reka_4.csv"
filename_5 = "acc_data_reka_5.csv"


#Kosc krzyżowa - W
# filename_1 = "acc_data_1.csv"
# filename_2 = "acc_data_2.csv"
# filename_3 = "acc_data_3.csv"
# filename_4 = "acc_data_4.csv"
# filename_5 = "acc_data_5.csv"

# Ręka - Natalia
# filename_1 = "acc_data_Natalia_1.csv"
# filename_2 = "acc_data_Natalia_2.csv"
# filename_3 = "acc_data_Natalia_3.csv"
# filename_4 = "acc_data_Natalia_4.csv"
# filename_5 = "acc_data_Natalia_5.csv"


list_filenames = [filename_1, filename_2, filename_3, filename_4, filename_5]


for file in list_filenames:

    accelerometer_data = read_data(file)
    accelerometer_data = replace_comma_with_dot(accelerometer_data)

    # accelerometer_cut = cut_non_gait_data(accelerometer_data[:,2], 100)
    # plt.plot(accelerometer_cut)
    # plt.title('Składowa acc_z docięta ' + file)
    # plt.show()
    mag = magnituda(accelerometer_data)
    plt.plot(mag)
    plt.title("Magnituda " + file)
    plt.show()
    accelerometer_filtered_data = filtering(mag,12,500,4)
    plt.plot(accelerometer_filtered_data)
    peaks = find_peak(accelerometer_filtered_data)
    plt.plot(peaks, accelerometer_filtered_data[peaks], "x")
    plt.title('Magnituda po filtrowaniu ' + file)
    plt.show()

    print(f'{file} steps={len(peaks)}')

    mean_of_window, variance, sd = moving_variance(accelerometer_filtered_data, 30)
    plt.subplot(3,1,1)
    plt.plot(mean_of_window)
    plt.title('średnia krocząca ' + file)
    plt.subplot(3,1,2)
    plt.plot(variance)
    plt.title('Wariancja krocząca ' + file)
    plt.subplot(3,1,3)
    plt.plot(variance)
    plt.title('Odchylenie standardowe kroczące ' + file)
    plt.show()



