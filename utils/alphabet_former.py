# coding=utf-8
import math
X = open("../data/dataset_labeled","r")
X_2 = open("../data/test_set_x.csv","r")
Y = open("../data/train_set_y.csv","r")
#get rid of the first line
Slovak = []
French = []
Spanish = []
German = []
Polish = []
All = []
Test = []
X.readline()
Y.readline()
#use 1/5 of the data as validation set
for line in X:
    lang = ((Y.readline()).split(","))[1]
    line = line.split(",")[1]
    #0: Slovak, 1: French, 2: Spanish, 3: German, 4: Polish
    All.append(line)
    if(int(lang) == 0):
        Slovak.append(line)
    elif (int(lang) == 1):
        French.append(line)
    elif (int(lang) == 2):
        Spanish.append(line)
    elif (int(lang) == 3):
        German.append(line)
    elif (int(lang) == 4):
        Polish.append(line)
    else:
        print ("Alien language detected")
for line in X_2:
    line = line.split(",")[1]
    Test.append(line)
#the splitted format will include line number
#build alphabet for each language and calculate the relative frequency of each letter


def alphabet_build(lan_list):
    lan_dict = {}
    for line in lan_list:
        chars = line.split()
        for char in chars:
            if char in lan_dict:
                lan_dict[char] = lan_dict[char]+1
            if char not in lan_dict:
                lan_dict[char] = 1
    #total = 1.00*sum(lan_dict.values())
    # for key, value in lan_dict.items():
    #     if lan_dict[key] <= 10:
    #         lan_dict.pop(key)
    print len(lan_dict)
    return lan_dict

def index_builder():
    Sl = alphabet_build(Slovak)
    Fr = alphabet_build(French)
    Sp = alphabet_build(Spanish)
    Ge = alphabet_build(German)
    Po = alphabet_build(Polish)
    Te = alphabet_build(Test)

    dict_merged = dict(Sl.items()+Fr.items()+Sp.items()+Ge.items()+Po.items())
    # print len(dict_merged)
    # for key, value in sorted(dict_merged.iteritems(), key=lambda (k,v): (v,k)):
    #     print "%s: %s" % (key, value)
    letter_index = {}
    index=0
    for key,item in dict_merged.items():
        letter_index[key] = index
        index += 1
    print len(letter_index)
    return letter_index

def idf_builder(letter_index):
    idf_list = [0]*len(letter_index)
    D = len(All)
    # print D
    for line in All:
        list_tmp = [0]*len(letter_index)
        chars = line.split()
        for char in chars:
            if letter_index.has_key(char):
                list_tmp[letter_index[char]] = 1
        idf_list = map(lambda (a, b): a + b, zip(idf_list, list_tmp))
    print idf_list
    for i in xrange(len(idf_list)):
        idf_list[i] = math.log(float(D) / (idf_list[i] + 1))

    print idf_list
    return idf_list

def alphabet_builder():
    Sl = alphabet_build(Slovak)
    Fr = alphabet_build(French)
    Sp = alphabet_build(Spanish)
    Ge = alphabet_build(German)
    Po = alphabet_build(Polish)
    return [Sl, Fr,Sp, Ge, Po]








