from __future__ import print_function

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from sklearn.preprocessing import OneHotEncoder
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

#--------prediction--------------
with open(TEST_FILE,"r") as test_reader:
    test_reader.readline()
    for line in test_reader:
        lang = line.split(",")[0]
        line = line.split(",")[1]
        line_vector = vectorzier(line)
        X_test.append(line_vector)
        y_test.append(int(lang))

# set parameters:
max_features = 108
maxlen = 1
batch_size = 32
embedding_dims = 50
filters = 250
kernel_size = 3
hidden_dims = 50
epochs = 2


print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')


print('Build model...')

model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(5, activation='softmax'))
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(X_test, y_test))

