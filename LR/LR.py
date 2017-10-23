from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import normalize

from utils import alphabet_former
from utils import reader
TRAIN_FILE = "../data/train_set_0.8"
TEST_FILE = "../data/test_set_0.2"
# TRAIN_FILE = "../data/dataset_labeled"
# TEST_FILE = "../data/test_set_x.csv"
PREDICTION = "predictions.csv"



letter_index = alphabet_former.index_builder()

# read data
data_reader = reader.Reader(TRAIN_FILE, TEST_FILE, letter_index)
X_train, y_train = data_reader.read_train()
X_test, y_test= data_reader.read_test(1)
# X_train = normalize(X_train, norm='l2')
# X_test = normalize(X_test, norm='l2')
# model definition
clf = LogisticRegression(solver='newton-cg',multi_class='multinomial')
clf.fit(X_train, y_train)

# prediction
predictions = clf.predict(X_test)

# evaluate
print accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)
print(cm)


# print len(X_test)
# with open(PREDICTION, 'w+') as prediction_writer:
#     cnt = 0
#     for prediction in predictions:
#         prediction_writer.writelines(str(cnt) + ',' + str(prediction) + '\n')
#         cnt += 1