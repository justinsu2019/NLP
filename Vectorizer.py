#what's in here:
'''
A- clean up the sentences in an file

B- 3 ways to vertorize:
1: basic way to check how many times a word appear in a sentence through all the acticle
2: ngram tell not only 1 word but also multiple words based on your selection
3: Tf-idf tells how many percentage of a word appear in a sentence, but sure what's the difference of it and the 1st way

'''

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re
import string
import nltk



#A----------------------------------------------------------------------------------------------------------------------------------
'''
### a longer way to clean up content ###
# how to clean up txt content
rawData = open('x.txt').read()
parsedData = rawData.replace(':', '\n').split('\n')
labelList = parsedData[0::2]
inputList = parsedData[1::2]
#print(labelList, InputList)

# create a dictionary for the content
Dictionary = pd.DataFrame({
    'label': labelList,
    'inputList': inputList
    })
print(Dictionary)
### a longer way to clean up content end ###
'''

### the very best way to clean up content ###
data = pd.read_csv("x.txt", sep=':', header = None)
data.columns = ['label','body_text']
#print(data)
### the very best way to clean up content end ###

stopwords = nltk.corpus.stopwords.words('english')
wn = nltk.WordNetLemmatizer()

### Vectorize your data ###

## clean up test function is here
def clean_text(rawData):
    stopword = nltk.corpus.stopwords.words('english')
    text_nopunct = "".join([char.lower() for char in rawData if char not in string.punctuation])
    tokenized_list = re.split('\W+', text_nopunct)
    text = [wn.lemmatize(word) for word in tokenized_list if word not in stopword]
    return text



#B----------------------------------------------------------------------------------------------------------------------------------

#1----------------------------------------------------------------------------------------------------------------------------------
# basic way to make word vector---------------------------------------------------------------------------------
### count how many times a word appear in a sentence ###
count_vect = CountVectorizer(analyzer = clean_text) # clearn_text is a handmade function
X_counts = count_vect.fit_transform(data['body_text'])
print(X_counts.shape)
print(count_vect.get_feature_names())

X_counts_df = pd.DataFrame(X_counts.toarray()) # till now we can see how many times a word appeared in a sentence
X_counts_df.columns = count_vect.get_feature_names()
print(X_counts_df)
### count how many times a word appear in a sentence end ###
# basic way to make word vector end ---------------------------------------------------------------------------------


#2----------------------------------------------------------------------------------------------------------------------------------

# With N-grams ---------------------------------------------------------------------------------
### count how many times [1,2,3](can be changed in below lines) words appear in a sentence ###
ngram_vect = CountVectorizer(ngram_range=(1,3))
X_counts = ngram_vect.fit_transform(data['body_text'])
print(X_counts.shape)
print(ngram_vect.get_feature_names())

X_counts_df = pd.DataFrame(X_counts.toarray())
print(X_counts_df)
X_counts_df.columns = ngram_vect.get_feature_names()
### count how many times [1,2,3](can be changed in below lines) words appear in a sentence end ###



#3----------------------------------------------------------------------------------------------------------------------------------
# TF-IDF ----------------------------------------------------------------------------------------
# need to learn more
'''
1st count how many times a word appear in a sentence
2nd count how many sentence including this word too
3rd show the percentage
below is in coding:
'''

from sklearn.feature_extraction.text import TfidfVectorizer

# this is the same as upper lines #
tfidf_vect = TfidfVectorizer(analyzer=clean_text)
X_tfidf = tfidf_vect.fit_transform(data['body_text'])
print(X_tfidf.shape)
print(tfidf_vect.get_feature_names())

# make it visilized so better to check out
X_tfidf_df = pd.DataFrame(X_tfidf.toarray())
X_tfidf_df.columns = tfidf_vect.get_feature_names()
print(X_tfidf_df)

# this is the same as upper lines end #




'''
def count_punct(text):
   count = sum([l for char in text if char in string.punctuation])
   return round(count/(len(text)-text.count(" "),3)* 100%

data['punct%'] = data['body_text'].apply(lambda x: count_punct(x))
#data['body_len'] = data['body_text'].apply(lambda x:len(x) - x.count(' '))

'''
