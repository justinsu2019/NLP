#what's in here:
'''
1 try to locate the pattern of the data
2( may not need 2) find what's the difference between the label data and the rest.
3 transform the data into better pattern to help doing the analyz, such as: square root it
4 let machine analyzs what's the difference of them.
'''

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re
import string
import nltk

stopwords = nltk.corpus.stopwords.words('english')
wn = nltk.WordNetLemmatizer()

data = pd.read_csv("x.txt", sep=':', header = None)
data.columns = ['label','body_text']

def count_punct(text):
   count = sum([1 for char in text if char in string.punctuation])
   return round(count/(len(text)-text.count(" ")),3)* 100

data['body_len'] = data['body_text'].apply(lambda x: len(x) - x.count(' '))
data['punct%'] = data['body_text'].apply(lambda x: count_punct(x))

print(data)


# checkout which feature may help in real task
# compare the length of the inputs, that will work if the length is truly a important feature.
from matplotlib import pyplot
import numpy as np
bins = np.linspace(0,100,40)

pyplot.hist(data[data['label']=='girl']['punct%'], bins, alpha=0.5, normed=True, label='girl')
pyplot.hist(data[data['label']=='boy']['punct%'], bins, alpha=0.5, normed=True, label='boy')
pyplot.title("girl vs boy punct%")
pyplot.legend(loc='upper left')
pyplot.show()


bins = np.linspace(0,200,40)

pyplot.hist(data[data['label']=='girl']['body_len'], bins, alpha=0.5, normed=True, label='girl')
pyplot.hist(data[data['label']=='boy']['body_len'], bins, alpha=0.5, normed=True, label='boy')
pyplot.title("girl vs boy body_len")
pyplot.legend(loc='upper left')
pyplot.show()


# transformation, make data easier to analyze
for i in range(4):
    pyplot.hist((data['punct%']**(1/(i+1))), bins=10)
    pyplot.title("Transformation: 1/{}".format(str(i+1)))
    pyplot.show()
