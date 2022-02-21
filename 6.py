import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# нарезание датасета
from sklearn.neighbors import KNeighborsClassifier
print("Первая")
dataset = pd.read_csv('file_name2.txt', sep=":")
dataset = dataset.drop("Ник", axis=1)
dataset.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
X = dataset.values[:, 0:10]
Y = dataset.values[:, 10]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2)
# learning реализация метода обучения
print("MVC")
from sklearn import svm
model = svm.SVC(kernel='poly', degree=2)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
Y1_predict = model.predict(X_test)
print(model.score(X_test,Y1_predict))
# 2 metod
print("----")
print("KNeighborsClassifier")
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
print(classifier.score(X_test, y_test))
Y2_predict = classifier.predict(X_test)
print(classifier.score(X_test, Y2_predict))
print("----")
print("naive_bayes")
# 3 metod
from sklearn.naive_bayes import MultinomialNB
models = MultinomialNB().fit(X_train, y_train)
print(models.score(X_test, y_test))
Y3_predict = models.predict(X_test)
print(models.score(X_test, Y3_predict))
print("----")
# from sklearn.cluster import KMeans
    # KMeans = KMeans(n_clusters=6, init,random_state=0)
    # KMeans.score(X_train,y_train)
    # KMeans.fit(X_train, y_train)

    # для оценивания
print("----")
print("Вторая")
print("MVC")
#синтезированные
dataset2 = pd.read_csv('file_name3.txt', sep=":")
dataset2 = dataset2.drop("Ник", axis=1)
dataset2.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
X = dataset2.values[:, 0:10]
Y = dataset2.values[:, 10]
X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X,
    Y,
    test_size=0.2)
#
print(model.score(X_test2, y_test2))
Y1_predict2 = model.predict(X_test2)
print(model.score(X_test2, Y1_predict2))
#
print("----")
print("KNeighborsClassifier")
print(classifier.score(X_test2, y_test2))
Y2_predict2 = classifier.predict(X_test2)
print(classifier.score(X_test2, Y2_predict2))
print("----")
print("naive_bayes")
print(models.score(X_test2, y_test2))
Y3_predict2 = models.predict(X_test2)
print(models.score(X_test2, Y3_predict2))
print("---")
print("---")
