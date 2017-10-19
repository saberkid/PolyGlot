# coding=utf-8
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from utils import alphabet_former
from utils import reader
import numpy as np
TRAIN_FILE = "../data/train_set_0.6"
TRAIN_FILE_2 = "../data/train_set_0.2"
TEST_FILE = "../data/test_set_0.2"
# TRAIN_FILE = "../data/dataset_labeled"
# TEST_FILE = "../data/test_set_x.csv"
PREDICTION = "predictions_3.csv"

letter_index = alphabet_former.index_builder()

# read data
data_reader = reader.Reader(TRAIN_FILE, TEST_FILE, letter_index)
data_reader2 = reader.Reader(TRAIN_FILE_2, TEST_FILE, letter_index)
X_train, y_train = data_reader.read_train()
X_test, y_test = data_reader.read_test(1)
X_train_2, y_train_2 = data_reader2.read_train()


# model definition
clf_nb = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf_lr = LogisticRegression()
clf_nb.fit(X_train, y_train)
clf_lr.fit(X_train, y_train)
# predict sub-model
predictions_lr = clf_lr.predict(X_train_2)
predictions_nb = clf_nb.predict(X_train_2)

# meta
y_predict = []
for i in xrange(len(predictions_lr)):
    y_predict.append([predictions_lr[i], predictions_nb[i]])
y_predict = np.asarray(y_predict)

clf_meta = XGBClassifier()
clf_meta.fit(y_predict, y_train_2)
# prediction
predictions_nb_test = clf_nb.predict(X_test)
predictions_lr_test = clf_lr.predict(X_test)
y_predict_test = []
for i in xrange(len(predictions_lr_test)):
    y_predict_test.append([predictions_lr_test[i], predictions_nb_test[i]])

y_predict_test = np.asarray(y_predict_test)

predictions_test = clf_meta.predict(y_predict_test)
print accuracy_score(y_test, predictions_test)
cm = confusion_matrix(y_test, predictions_test)
print(cm)
# print len(X_test)
# with open(PREDICTION, 'w+') as prediction_writer:
#     cnt = 0
#     for prediction in predictions:
#         prediction_writer.writelines(str(cnt) + ',' + str(prediction) + '\n')
#         cnt += 1
