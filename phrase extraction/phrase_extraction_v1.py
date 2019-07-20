'''
What's new?
Logic updated. pick out 3-4 words from sentence and then search for the words in whole other sentences to decide whether it's a potential phrase

Function:
1) extract all the unique words from the whole acticle.
2) pick out the words appeared more than once in different sentence
3) check how many times a "phrase" appeared in every sentence
4) pick out those more than once in all
5) pick out those in phrase pool & not in but appears a lot of times, need manual checking.
6)? put the others not in phrase pool into our database automatically

needs:
1 build our phrase pool,
2 build a pool shows those obviously not phrase
3 check if the phrase in function 3 is in our pool, if it is then don't have to check how many times it appears in whole acticle.
4 check if any phrase in our pool in the acticle but only appeared once.
5 automatically let machine decide if a new phrase should be added into the pool
'''

'''
proceduce:
1 计算每个word在所有句子里出现的次数
2 从最多的开始，查以他为开始后续出现的word超过1次的次数，
3 如此重复，把所有的超过1次的单词组合都找出来
4 反馈出来result在已有短语数据库里查询, 未查到则记录在数据库里，后续update

'''

import acticle_process_tool as apt
import re


#x = [["I","am","the","one","or","not"],["I","doult","it"],["don't","have","to"],["why","not"],["cause","I","am"],["Let","us","see"]]

x = "In the last four years, there's been an increase in drug cartels from Central and South America using these semi-submersible vessels, Lt. Commander Stephen Brickey told CNN. These vessels are relatively rare. They re expensive to build, and cartels have to build them deep in jungles to avoid detection. Once they're filled with drugs and deployed, Brickey said they're almost impossible to detect without prior intelligence or an aircraft. 'They blend in,' he said. 'Most of the vessel is underwater, so it's hard to pick out. They're painted blue. They match the water.' Even if the Coast Guard does manage to catch the vessel, they have to be quick. Every vessel is built with the ability to sink and destroy the evidence within minutes, with the smugglers knowing that the Coast Guard will make sure they don't drown, Brickey said. The smugglers could also be armed. It's not easy, and the Coast Guard only stops an estimated 11 percent of the vessels that pass through the East Pacific -- an area Brickey said was about the size of the entire US. The Coast Guard, he said say, is tasked with patrolling the area with the equivalent of two police cars. And a part of of the problem is that 70 percent of Coast Guard's fleet is over 50 years old -- so they're slow and require a lot of maintenance before they can be deployed. 'They're not really effective enough to meet this new threat,' Brickey said. The five people involved were sent to the DEA for prosecution In the filmed incident, the Coast Guard was able to detect the vessel with an aircraft, who relayed the information to members on the ground. Once they had an idea of where the vessel was, the guard launched two small boats to creep up on the smugglers, and were eventually able to board without detection. There were five people on the vessel, who were then turned over the US Drug Enforcement Administration for prosecution. The bust was the first time the Coast Guard used a new type of ship on a counter-drug patrol, and Brickey said the incident is a great example of what these new ships can do.'These sorts of capabilities on these ships is what will make us successful in the future,' he said. This story has been updated with new numbers for the amount of cocaine seized."

with open("sophie.txt","r",encoding='gbk',errors='ignore') as f:
    x = f.read()
print("x is {}\n:".format(x))

'''
from nltk.collocations import *
trigram_measures = nltk.collocations.TrigramAssocMeasures()
text = "i would't have the Scotland Yarders know it for the world"
tokens = nltk.wordpunct_tokenize(text)
finder = TrigramCollocationFinder.from_words(tokens)
scored = finder.score_ngrams(trigram_measures.raw_freq)
sorted(bigram for bigram, score in scored)
'''

def phrase_extraction(x):

    appear_times = 0
    word_appear_time_dic = {}
    y, unique_words = [], []

    x = apt.create_wordlist_in_sentence(apt.sparate_acticles_into_sentence(x)) # get input acticle into wordlist by sentence

    print(len(x))
    
    #1 function ----------------------------------------------------------------------------------------------------
    for sentence in x:
        [y.append(word.lower()) for word in sentence if word not in y]
    #print("y is",y)

    '''
    in new logic, we don't need to do function 2.
    #2 function ----------------------------------------------------------------------------------------------------
    # pick out those words appeared more than once in the article.
    for word_unique in y:
            for sentence in x:
                appear_times += (word_unique in sentence and 1)
            word_appear_time_dic[word_unique]= appear_times
            if appear_times > 1 and word_unique not in unique_words:
                unique_words.append(word_unique)
            appear_times = 0
    print("\nunique_words is ",unique_words)
    '''

    #3 function ----------------------------------------------------------------------------------------------------

    phrase_pool = {}

    def phrase_pool_filling(x):

        for sentence in x:
                for i in range(len(sentence)):
                    for j in range(i+1,len(sentence)):
                        for k in range(j+1,len(sentence)):
                            appear_times = 0
                            for sentence_searching in x:
                                if sentence[i] in sentence_searching and sentence[j] in sentence_searching[i:] and sentence[k] in sentence_searching[j:]:
                                    appear_times += 1
                            #if (sentence[i]+" "+sentence[j]+" "+sentence[k] in phrase_pool):
                                #phrase_pool[(sentence[i]+" "+sentence[j]+" "+sentence[k])] = appear_times + phrase_pool.get(sentence[i]+" "+sentence[j]+" "+sentence[k])
                            if appear_times > 1 and (sentence[i]+" "+sentence[j]+" "+sentence[k] not in phrase_pool):
                                phrase_pool[(sentence[i]+" "+sentence[j]+" "+sentence[k])] = appear_times
                            appear_times = 0
                            
                            for l in range(k+1,len(sentence)):
                                appear_times = 0
                                for sentence_searching in x:
                                    if sentence[i] in sentence_searching and sentence[j] in sentence_searching[i:] and sentence[k] in sentence_searching[j:] and sentence[l] in sentence_searching[k:]:
                                        appear_times += 1
                                #if ((sentence[i]+" "+sentence[j]+" "+sentence[k]+" "+sentence[l]) in phrase_pool):
                                    #phrase_pool[(sentence[i]+" "+sentence[j]+" "+sentence[k]+" "+sentence[l])] = appear_times + phrase_pool.get(sentence[i]+" "+sentence[j]+" "+sentence[k]+" "+sentence[l])
                                if appear_times > 1 and (sentence[i]+" "+sentence[j]+" "+sentence[k]+" "+sentence[l] not in phrase_pool):
                                        phrase_pool[(sentence[i]+" "+sentence[j]+" "+sentence[k]+" "+sentence[l])] = appear_times
                            appear_times = 0
        return phrase_pool


    def phrase_pool_filling_stepbystep(x):
        i = 0
        while (i+100)<=len(x):
            phrase_pool_filling(x[i:i+100])
            i += 100
            #print("the {} times Phrase pool is \n {} \n".format(i, phrase_pool))
        phrase_pool_filling(x[i:])
        #print("the final Phrase pool is \n {} \n".format(phrase_pool))

    phrase_pool_filling_stepbystep(x)


    # 5 function ----------------------------------------------------------------------------------------------------
    our_phrase_pool = ["the more the better", "as we thought","the an of"] 

    phrase = list(set(our_phrase_pool).intersection(set(phrase_pool.keys()))) # pick out which both in phrase_pool and phrase_final
 
    phrase_need_manual_check = {}
    for i in phrase_pool.keys():
        if phrase_pool.get(i) > 3 and i not in our_phrase_pool:
            phrase_need_manual_check[i] = phrase_pool.get(i)
    phrase_need_manual_check = sorted(phrase_need_manual_check.items(),key=lambda phrase_need_manual_check:phrase_need_manual_check[1],reverse=True)

    f = open('result.txt','a')
    f.write(str(phrase_need_manual_check))
    f.write("\n")
    f.write(str(phrase))
    f.close()
  
    #print("1 phrase_need_manual_check are here \n {} \n".format(phrase_need_manual_check))
    #print("2 extracted phrase are: \n {} \n".format(phrase))
    return phrase #phrase_final
   
if __name__ == '__main__':
    phrase_extraction(x)

