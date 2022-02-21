from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
# load data
dataset = pd.read_csv('file_name2.txt', sep=":")
#dataset.columns = ["Ник", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dataset= dataset.drop("Ник", axis=1)
array = dataset.values
X = array[:,0:10]
Y = array[:,10]
# feature extraction

model = ExtraTreesClassifier()

model.fit(X, Y)

print(model.feature_importances_)