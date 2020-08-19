# keras module for building LSTM
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
from keras.models import Sequential
import keras.utils as ku

# set seeds for reproducability
import tensorflow
from numpy.random import seed

tensorflow.random.set_seed(2)
seed(1)

import pandas as pd
import numpy as np
import string, os

import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)


def clean_text(txt):
    txt = "".join(v for v in txt if v not in string.punctuation).lower()
    txt = txt.encode("utf8").decode("ascii", 'ignore')
    return txt

class ChatAI:
    def __init__(self):
        pass

    def train(self, messages):
        corpus = [clean_text(x) for x in messages]



corpus = [clean_text(x) for x in all_headlines]
print(len(messages))
