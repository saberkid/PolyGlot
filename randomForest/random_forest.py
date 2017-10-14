# coding=utf-8

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from utils import alphabet_former

TRAIN_FILE = "../data/train_set_0.8"
TEST_FILE = "../data/test_set_0.2"
# TRAIN_FILE = "../data/dataset_labeled"
# TEST_FILE = "../data/test_set_x.csv"
PREDICTION = "predictions.csv"
def vectorzier(line):
    letters = line.split(' ')
    letters = letters[0:min(len(letters), 20)]
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
    while 1:
        line = train_reader.readline()
        if not line:
            break
        (lang,line) = line.split(",")[0], line.split(",")[1]

        if len(line)<=1:
            continue
        line_vector = vectorzier(line)
        X_train.append(line_vector)
        y_train.append(int(lang))

clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train)



#--------prediction--------------
with open(TEST_FILE,"r") as test_reader:
    test_reader.readline()
    for line in test_reader:
        lang = line.split(",")[0]
        line = line.split(",")[1]
        line_vector = vectorzier(line)
        X_test.append(line_vector)
        y_test.append(int(lang))
#----------------------------------
# with open(TEST_FILE,"r") as test_reader:
#     for line in test_reader:
#         line = line.split(",")[1]
#         line_vector = vectorzier(line)
#         X_test.append(line_vector)

predictions = clf.predict(X_test)
print accuracy_score(y_test, predictions)


# print len(X_test)
# with open(PREDICTION, 'w+') as prediction_writer:
#     cnt = 0
#     for prediction in predictions:
#         prediction_writer.writelines(str(cnt) + ',' + str(prediction) + '\n')
#         cnt += 1
