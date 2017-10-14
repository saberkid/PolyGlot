# coding=utf-8
import numpy as np
from xgBoost import XGBClassifier

from utils import alphabet_former

# TRAIN_FILE = "../data/train_set_0.8"
# TEST_FILE = "../data/test_set_0.2"
TRAIN_FILE = "../data/dataset_labeled"
TEST_FILE = "../data/test_set_x.csv"
PREDICTION = "predictions.csv"
def vectorzier(line):
    letters = line.split(' ')
    letter_vector = [0] * len(letter_index)
    for letter in letters:
        if letter_index.has_key(letter):
            letter_vector[letter_index[letter]] += 1
    return letter_vector

X_train = []
X_test = []
y_train = []
y_test = []
letter_index = alphabet_former.index_builder()


with open(TRAIN_FILE,"r") as train_reader:
    train_reader.readline()
    for line in train_reader:
        lang = line.split(",")[0]
        line = line.split(",")[1]
        line_vector = vectorzier(line)
        X_train.append(line_vector)
        y_train.append(int(lang))


X_train = np.asarray(X_train)
y_train = np.asarray(y_train)
clf = XGBClassifier()
clf.fit(X_train, y_train)



#--------prediction--------------
# with open(TEST_FILE,"r") as test_reader:
#     test_reader.readline()
#     for line in test_reader:
#         lang = line.split(",")[0]
#         line = line.split(",")[1]
#         line_vector = vectorzier(line)
#         X_test.append(line_vector)
#         y_test.append(int(lang))
# X_test = np.asarray(X_test)
# y_test = np.asarray(y_test)
################################
with open(TEST_FILE,"r") as test_reader:
    for line in test_reader:
        line = line.split(",")[1]
        line_vector = vectorzier(line)
        X_test.append(line_vector)
X_test = np.asarray(X_test)
predictions = clf.predict(X_test)
# print accuracy_score(y_test, predictions)
# print len(X_test)
with open(PREDICTION, 'w+') as prediction_writer:
    cnt = 0
    for prediction in predictions:
        prediction_writer.writelines(str(cnt) + ',' + str(prediction) + '\n')
        cnt += 1
