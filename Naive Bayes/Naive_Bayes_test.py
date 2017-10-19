# coding=utf-8
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from utils import alphabet_former
from utils import reader
TRAIN_FILE = "../data/train_set_0.8"
TEST_FILE = "../data/test_set_0.2"
# TRAIN_FILE = "../data/dataset_labeled"
# TEST_FILE = "../data/test_set_x.csv"
PREDICTION = "predictions_3.csv"



letter_index = alphabet_former.index_builder()

# read data
data_reader = reader.Reader(TRAIN_FILE, TEST_FILE, letter_index)
X_train, y_train = data_reader.read_train()
X_test, y_test= data_reader.read_test(1)

# model definition
clf = MultinomialNB()
clf.fit(X_train, y_train)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)


# prediction
predictions = clf.predict(X_test)

#      evaluate
print accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)
print(cm)

# print len(X_test)
# with open(PREDICTION, 'w+') as prediction_writer:
#     cnt = 0
#     for prediction in predictions:
#         prediction_writer.writelines(str(cnt) + ',' + str(prediction) + '\n')
#         cnt += 1
