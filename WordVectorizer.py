from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

data = pd.read_csv("x.txt", sep='\t')
data.columns = ['label','body_text']


count_vect = CountVectorizer(analyzer = clearn_text) # clearn_text is a handmade function
X_counts = count_vect.fit_transform(data['body_text'])
print(X_counts.shape)
print(count_vect.get_feature_name())

X_counts_df = pd.DataFrame(X_counts_sample.toarray()) # till now we can see how many times a word appeared in a sentence


# With N-grams ---------------------------------------------------------------------------------
ngram_vect = CountVectorizer(ngram_range=(1,3))
X_counts = ngram_vect.fit_transform(data['body_text'])
print(X_counts.shape)
print(ngram_vect.get_feature_name())

X_counts_df = pd.DataFrame(X_counts_sample.toarray())
X_counts_df.columns = ngram_vect.get_feature_names()

'''
# TF-IDF ----------------------------------------------------------------------------------------
# need to learn more
1st count how many times a word appear in a sentence
2nd count how many sentence including this word too
3rd show the percentage

below is in coding:
'''
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vect = TfidfVectorizer(analyzer=clean_text)
X_tfidf = tfidf_vect.fit_transform(data['body_text'])
print(X_tfidf.shape)
print(tfidf_vect.get_feature_names())


import string

def count_punct(text):
   count = sum([l for char in text if char in string.punctuation])
   return round(count/(len(text)-text.count(" "),3)* 100%

data['punct%'] = data['body_text'].apply(lambda x: count_punct(x))

data['body_len'] = data['body_text'].apply(lambda x:len(x) - x.count(' '))



