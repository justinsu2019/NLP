# Function
# 完美词型还原
# words clean up and trans back to the original writing.

import re
import pandas as pd
import string
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet

# change x to change inputs
x = "i've never had such a great time before, 1 whole week, sleeping, hiking is so amazingly good. I love my wife and she was going together with me, which I feel so good all the time."

ps = nltk.PorterStemmer()
wn = nltk.WordNetLemmatizer()

# 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

tokens = word_tokenize(x)  # 分词
text_nopunct = " ".join([char.lower() for char in tokens if (char.isspace() or char.isalpha()) and (char not in string.punctuation)])
tokenized_list = re.split('\W+', text_nopunct)
tagged_sent = pos_tag(tokenized_list)     # 获取单词词性
lemmas_sent = []
for tag in tagged_sent:
    wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
    lemmas_sent.append(wn.lemmatize(tag[0], pos=wordnet_pos)) # 词形还原
print(lemmas_sent)


# for single words translation -----------------------------------------------------

import re
import pandas as pd
import string
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet

# change x to change inputs
x = "stopped"
a = []

ps = nltk.PorterStemmer()
wn = nltk.WordNetLemmatizer()

# 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

tag = pos_tag(re.split('\W+', x))     # 获取单词词性
wordnet_pos = get_wordnet_pos(tag[0][1]) or wordnet.NOUN
print(wn.lemmatize(tag[0][0], pos=wordnet_pos)) # 词形还原
