import numpy
import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler
import pydbgen
import numpy as np
from pydbgen import pydbgen
myDB=pydbgen.pydb()

#конверт данные из xls файла в txt
xl = pd.ExcelFile("Survey.xls")
xl.sheet_names
for sheet in xl.sheet_names:
    file = pd.read_excel(xl, sheet_name=sheet)
    file.to_csv('Survey.txt', header=True, index=False, sep=":")
# загрузка файлов из txt файла
dataset = pd.read_csv('Survey.txt', sep=":")
# поменял столбцы, чтобы было удобно
dataset.columns = ["Ник", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
testdf = myDB.gen_dataframe(500,['name'])
df = pd.DataFrame(np.random.randint(0,11,size=(500, 10)), columns=list('123456789A'))
df.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    testdf[i + 1] = df[i+1]
testdf.columns = ["Ник", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dataset=testdf
#замена NaN на -1
dataset = dataset.replace(-1, numpy.NaN)
# замена с -1 на сред.ариф
dataset = dataset.fillna(dataset.mean())
# проверка на нормальные данные (#1провести алгоритм очистки от грязных данных по горизонтали DataSet)
for X in range(1,11):
    filter = dataset[X]>-1
    filter2 = dataset[X]<11
    dataset = dataset.where(filter & filter2)
# дроп NaN после проверки
dataset = dataset.dropna()
# создание  временной DataFrame
data = dataset
# чтобы удалить столбец Ник
data = data.drop("Ник", axis=1)
#провести алгорим нормализации данных
trans = StandardScaler()
data = trans.fit_transform(data)
data = pd.DataFrame(data)
#камбэк столбца Ник
Nick = dataset['Ник']
test = dataset
for i in range(10):
    test = test.drop(i + 1, axis=1)
for i in range(10):
    test[i + 1] = data[i]
# минус дубликаты(повторяющие записи) #2провести алгоритм очистки от грязных данных по горизонтали DataSet
test = test.drop_duplicates(subset=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
dataset = dataset.drop_duplicates(subset=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#запись на файл
dataset.to_csv('file_name.txt',header=True, index=False, sep=":")