import pandas as pd
import numpy as np
# написать программный код для высчитывания целевых переменных (дополнительных инфломативных признаков из существующих полей DataSet).
# dataset = pd.read_csv('file_name.txt', sep=":")
dataset = pd.read_csv('file_name.txt', sep=":")
dataset.columns = ["Ник", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Создание нескольких целевых переменных, путем объединения вопросов
#dataset['11'] = round(dataset[2] + dataset[4] + dataset[5])
#dataset['12'] = round(dataset[1] + dataset[3] + dataset[6] + dataset[7])
#dataset['13'] = round(dataset[8] + dataset[9] + dataset[10])
#dataset['14'] = round((dataset['11']/3) + (dataset['12']/3) + (dataset['13']/3)/3)
dataset.loc[(dataset[2] > 4) & (dataset[4] > 4) & (dataset[5] > 4), 'Regrator'] = 1
dataset.loc[(dataset[1] > 4) & (dataset[3] > 4) & (dataset[6] > 4), 'Regrator'] = 2
dataset.loc[(dataset[8] > 4) & (dataset[9] > 4) & (dataset[10] > 4), 'Regrator'] = 3
#dataset.loc[(dataset[2] > 4) & (dataset[4] > 4) & (dataset[5] > 4), 'Regrator'] = 4
#dataset.loc[(dataset[7] > 4), 'Regrator'] = 5
dataset = dataset.replace(np.NaN, 4)
# запись
dataset.to_csv('file_name4.txt', header=True, index=False, sep=":")
