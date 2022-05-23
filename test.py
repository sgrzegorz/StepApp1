import os
from os import walk
from main import znajdz_szczyty
from matplotlib import pyplot as plt

from functionalities import read_data, replace_comma_with_dot
from preprocessing import magnituda, filtering, find_peak

for directory in os.listdir('kroki'):
    files = []
    for (dirpath, dirnames, filenames) in walk(f'kroki/{directory}'):
        files.extend(filenames)
    # print(f'Dir {directory}:')
    # print(files)
    # print('-------')

    real_steps = int(directory)

    errors = []
    ok = []
    nearly_ok =[]
    for file in files:

        (peaks,accelerometer_filtered_data) = znajdz_szczyty(f'kroki/{directory}/{file}')

        steps = len(peaks)
        if steps != real_steps:
            errors.append(file)

        if steps == real_steps:
            ok.append(file)

        if steps == real_steps or steps == (real_steps+1) or steps == (real_steps-1):
            nearly_ok.append(file)

        # print(f'{steps}/{real_steps} {file}')

    print(f'Poprawnie znaleziono:{len(ok)/len(files)*100:.2f}%')
    print(f'Prawie poprawne znaleziono:{len(nearly_ok)/len(files)*100:.2f}% (dopuszczalna pomyłka o 1 krok) ')


    for file in errors:
        (peaks, accelerometer_filtered_data) = znajdz_szczyty(f'kroki/{directory}/{file}')

        plt.plot(accelerometer_filtered_data)
        plt.plot(peaks, accelerometer_filtered_data[peaks], "x")
        plt.title(f'{len(peaks)}/{real_steps} {file}')
        plt.show()
