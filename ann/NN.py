import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from sklearn.preprocessing import normalize
from utils import alphabet_former
from sklearn.metrics import confusion_matrix
from utils import reader
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE

TRAIN_FILE = "../data/train_set_0.8"
TEST_FILE = "../data/test_set_0.2"
# TRAIN_FILE = "../data/dataset_labeled"
# TEST_FILE = "../data/test_set_x.csv"
PREDICTION = "predictions.csv"

map = {0:[1, 0, 0, 0, 0], 1:[0, 1, 0, 0, 0], 2:[0, 0, 1, 0, 0], 3:[0, 0, 0, 1, 0], 4:[0, 0, 0, 0, 1]}

letter_index = alphabet_former.index_builder()

# read data
data_reader = reader.Reader(TRAIN_FILE, TEST_FILE, letter_index)
X_train, y_train = data_reader.read_train()
X_test, y_test = data_reader.read_test(0)

# oversampling the training set
sm = SMOTE(random_state=42)
X_train, y_train = sm.fit_sample(X_train, y_train)
print('Resampled dataset shape%d'%len(y_train))

# normalize
X_train_normalized = normalize(X_train, norm='l2')
X_test_normalized = normalize(X_test, norm='l2')

# onehot encoding for y
y_train_onehot = []
y_test_onehot = []
for i in xrange(len(y_train)):
    y_train_onehot.append(map[y_train[i]])
for i in xrange(len(y_test)):
    y_test_onehot.append(map[y_test[i]])

y_train_onehot = np.asarray(y_train_onehot)
y_test_onehot = np.asarray(y_test_onehot)
# set parameters:
max_features = 640
hiddens = 16
batch_size = 32
epochs = 2


print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')
print('Build model...')

model = Sequential()
model.add(Dense(hiddens, input_dim=max_features, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(5, activation='softmax'))
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.load_weights('1.h5')
model.fit(X_train_normalized, y_train_onehot,
          batch_size=batch_size,
          epochs=epochs)

model.save_weights('1.h5')



predictions = model.predict_classes(X_test_normalized)

print accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)
print cm


# reomove comment for test

# with open(PREDICTION, 'w+') as prediction_writer:
#     cnt = 0
#     for prediction in predictions:
#         prediction_writer.writelines(str(cnt) + ',' + str(prediction) + '\n')
#         cnt += 1
