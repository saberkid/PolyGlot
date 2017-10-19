# coding=utf-8
# from nltk.tokenize import TweetTokenizer
# tknzr = TweetTokenizer()
import re
import csv
import sys
from sklearn.preprocessing import OneHotEncoder

DATASET_TRAIN_X = 'data/train_set_x.csv'
DATASET_TRAIN_Y = ''
DATASET_TRAIN_X_CLEANED = 'data/train_set_x_cleaned_nothing.csv'


def data_cleaner(text):
    text = ''.join([i for i in text if not i.isdigit()])  # remove digits
    text = text.replace('\n', '').lower()
    text_unicode = text.decode('utf-8')
    emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
        "+", flags=re.UNICODE)
    #text_clean = emoji_pattern.sub(r'', text_unicode)  # no emoji
    #text_clean = re.sub(r'[^\w+]', '', text_clean, flags=re.UNICODE) #no symbol
    return text_unicode#.encode('utf-8')


def data_tokenizer():
    with open(DATASET_TRAIN_X) as train_x, open(DATASET_TRAIN_X_CLEANED, 'wb+') as train_x_cleaned:
        r_csv = csv.reader(train_x)
        w_csv = csv.writer(train_x_cleaned)
        for row in r_csv:
            text_line = row[1]
            text_cleaned = data_cleaner(text_line)
            text_cleaned = u' '.join([i for i in text_cleaned if i != ' ']).encode('utf-8')  # tokenize
            row = [row[0], text_cleaned]
            w_csv.writerow(row)

data_tokenizer()