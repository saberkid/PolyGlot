# Input:      newInput: vector to compare to existing dataset (1xN)
#             dataSet:  size m data set of known vectors (NxM)
#             labels:   data set labels (1xM vector)
#             k:        number of neighbors to use for comparison

# Output:     the most popular class label
#########################################

from numpy import *
from utils import reader
from utils import alphabet_former
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

TRAIN_FILE = "../data/train_set_0.8"
TEST_FILE = "../data/test_set_0.2"
# TRAIN_FILE = "../data/dataset_labeled"
# TEST_FILE = "../data/test_set_x.csv"
PREDICTION = "predictions_3.csv"

letter_index = alphabet_former.index_builder()

data_reader = reader.Reader(TRAIN_FILE, TEST_FILE,letter_index)
X_train, y_train = data_reader.read_train()
X_test, y_test = data_reader.read_test(1)

nbrs = KNeighborsClassifier(n_neighbors=5, algorithm='ball_tree')
nbrs.fit(X_train, y_train)
predictions = nbrs.predict(X_test)

print accuracy_score(y_test, predictions)

