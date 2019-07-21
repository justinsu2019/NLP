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

wn = nltk.WordNetLemmatizer()

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t', header = None)
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
#X_tfidf_df = pd.DataFrame(X_tfidf.toarray())
#X_tfidf_df.columns = tfidf_vect.get_feature_names()
X_feature = pd.concat([data['body_len'],data['punct%'], pd.DataFrame(X_tfidf.toarray())],axis =1)
#print(X_tfidf_df)



# build a random forest model by machine learning, not deep learning.
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_feature, data['label'],test_size=0.2)

def train_GB(est, max_depth, lr):
   gb = GradientBoostingClassifier(n_estimators=est, max_depth=max_depth, learning_rate=lr)
   gb_model = gb.fit(X_train, y_train)
   y_pred = gb_model.predict(X_test)
   precision, recall,fscore,support = score(y_test, y_pred,pos_label='spam',average='binary')
   print('Est:{} / Depth:{} / LR:{} ---precision:{} / recall:{} / accuracy:{}'.format(

      est, max_depth,lr,round(precision, 3), round(recall, 3), round((y_pred==y_test).sum()/len(y_pred), 3)))


for n_est in [50, 100, 150]:
   for max_depth in [3,7,11,15]:
      for lr in [0.01, 0.1, 1]:
         train_GB(n_est, max_depth, lr)

