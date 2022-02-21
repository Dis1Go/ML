import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from random_username.generate import generate_username
dataset = pd.read_csv('file_name4.txt', sep=":")
dataset= dataset.drop("Ник", axis=1)
array = dataset.values
X = array[:,0:10]
Y = array[:,10]
reg = LinearRegression().fit(X, Y)
r2 =reg.score(X,Y)
test_R = reg.predict(X)
rows, cols = (500, 10)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(int(np.random.choice(test_R)))
    arr.append(col)

dataset = pd.DataFrame(arr)
dataset.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Создание нескольких целевых переменных, путем объединения вопросов
dataset['X'] = dataset[2] + dataset[4] + dataset[5]
dataset['Y'] = dataset[1] + dataset[3] + dataset[6] + dataset[7]
dataset['Z'] = dataset[8] + dataset[9] + dataset[10]
#dataset['A'] = round((dataset['X']/3) + (dataset['Y']/3) + (dataset['Z']/3)/3)
dataset.loc[(dataset[2] > 4) & (dataset[4] > 4) & (dataset[5] > 4), 'Regrator'] = 1
dataset.loc[(dataset[1] > 4) & (dataset[3] > 4) & (dataset[6] > 4), 'Regrator'] = 2
dataset.loc[(dataset[8] > 4) & (dataset[9] > 4) & (dataset[10] > 4), 'Regrator'] = 3
#dataset.loc[(dataset[2] > 4) & (dataset[4] > 4) & (dataset[5] > 4), 'Regrator'] = 4
#dataset.loc[(dataset[7] > 4), 'Regrator'] = 5
dataset = dataset.replace(np.NaN, 4)
nickname = generate_username(500)
data =pd.DataFrame(nickname)
for i in range(10):
    data[i + 1] = dataset[i+1]
data['Regrator'] = dataset['Regrator']
data.columns = ['Ник',1, 2, 3, 4, 5, 6, 7, 8, 9, 10,'Regrator']
data.to_csv('file_name5.txt', header=True, index=False, sep=":")
