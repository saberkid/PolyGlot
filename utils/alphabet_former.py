# coding=utf-8
#some code to separate the language from one another in order to better encode them
X = open("../data/train_set_x_cleaned.csv","r")
Y = open("../data/train_set_y.csv","r")
#get rid of the first line
Slovak = []
French = []
Spanish = []
German = []
Polish = []
X.readline()
Y.readline()
#use 1/5 of the data as validation set
for line in X:
    lang = ((Y.readline()).split(","))[1]
    line = (line.split(",")[1])
    #0: Slovak, 1: French, 2: Spanish, 3: German, 4: Polish
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

#the splitted format will include line number
#build alphabet for each language and calculate the relative frequency of each letter

# Sl, Fr, Sp, Ge, Po = {}
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
    for key, value in lan_dict.items():
        if lan_dict[key] <= 10:
            lan_dict.pop(key)
    print len(lan_dict)
    return lan_dict

def index_builder():
    Sl = alphabet_build(Slovak)
    Fr = alphabet_build(French)
    Sp = alphabet_build(Spanish)
    Ge = alphabet_build(German)
    Po = alphabet_build(Polish)

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






