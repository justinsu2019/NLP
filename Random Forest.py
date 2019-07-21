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

## clean up test function is here
def clean_text(rawData):
    stopword = nltk.corpus.stopwords.words('english')
    text_nopunct = "".join([char.lower() for char in rawData if char not in string.punctuation])
    tokenized_list = re.split('\W+', text_nopunct)
    text = [wn.lemmatize(word) for word in tokenized_list if word not in stopword]
    return text


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vect = TfidfVectorizer(analyzer=clean_text)
X_tfidf = tfidf_vect.fit_transform(data['body_text'])
#print(X_tfidf.shape)
#print(tfidf_vect.get_feature_names())

# make it visilized so better to check out
X_tfidf_df = pd.DataFrame(X_tfidf.toarray())
X_tfidf_df.columns = tfidf_vect.get_feature_names()
X_features = pd.concat([data['body_len'],data['punct%'], pd.DataFrame(X_tfidf.toarray())],axis =1)
#print(X_tfidf_df)



# build a random forest model by machine learning, not deep learning.
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=-1)
k_fold = KFold(n_splits=4)
score = cross_val_score(rf, X_features,data['label'],cv=k_fold, scoring='accuracy', n_jobs=-1)
print(score)



# build a random forest classifier

from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split
