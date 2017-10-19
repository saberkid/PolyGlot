import numpy as np

class Reader:
    def __init__(self,train_file, test_file, letter_index):
        self.train_file = train_file
        self.test_file = test_file
        self.letter_index = letter_index
        # self.idf_list = idf_list

    def vectorizer(self, line, mode=0): # 1: limit length to 20
        letters = line.split(' ')
        if mode:
            letters = letters[0:min(len(letters), 20)]
        letter_vector = [0] * len(self.letter_index)
        for letter in letters:
            if self.letter_index.has_key(letter):
                letter_vector[self.letter_index[letter]] += 1
         # letter frequency
        # for i in xrange(len(letter_vector)):
        #     letter_vector[i] = float(letter_vector[i])/len(letters)

        return letter_vector

    def read_train(self):
        X_train = []
        y_train = []
        with open(self.train_file, "r") as train_reader:
            while 1:
                line = train_reader.readline()
                if not line:
                    break
                (lang,line) = line.split(",")[0], line.split(",")[1]

                if len(line)<=1:
                    continue
                line_vector = self.vectorizer(line)
                X_train.append(line_vector)
                y_train.append(int(lang))
        X_train, y_train = np.asarray(X_train), np.asarray(y_train)
        return X_train, y_train

    def read_test(self, mode=1): #1:validation, 0:test
        X_test = []
        y_test = []
        with open(self.test_file,"r") as test_reader:
            if mode:
                for line in test_reader:
                    lang = line.split(",")[0]
                    line = line.split(",")[1]
                    line_vector = self.vectorizer(line,0)
                    X_test.append(line_vector)
                    y_test.append(int(lang))
                X_test, y_test = np.asarray(X_test), np.asarray(y_test)
                return X_test, y_test
            else:
                for line in test_reader:
                        line = line.split(",")[1]
                        line_vector = self.vectorizer(line)
                        X_test.append(line_vector)
                X_test = np.asarray(X_test)
                return X_test
