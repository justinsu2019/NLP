x = [["I","am","the","one","or","not"],["I","doult","it"],["don't","have","to"],["why","not"],["cause","I","am"],["Let","us","see"]]
y = []

'''
1 计算每个word在所有句子里出现的次数
2 从最多的开始，查以他为开始后续出现的word超过1次的次数，
3 如此重复，把所有的超过1次的单词组合都找出来
4 反馈出来result在已有短语数据库里查询, 未查到则记录在数据库里，后续update

'''

appear_times = 0

word_appear_time_dic = {}
phrase_potential = []

#1
for sentence in x:
    [y.append(word) for word in sentence]
#print(y)
y_temp = list(set(y))
y_temp.sort(key = y.index)
#print(y_temp)

# need to update:--------------
for word_unique in y:
        for sentence in x:
            if word_unique in sentence:
                appear_times += 1
        #print(appear_times,"\n")
        word_appear_time_dic[word_unique]= appear_times
        if appear_times > 1 and word_unique not in phrase_potential:
            phrase_potential.append(word_unique)
        appear_times = 0

print("the phrase_potential is {}, and word_appear_time_dic is {}".format(phrase_potential,word_appear_time_dic))   #word_appear_time_dic



#2
phrase_pool = []

print("range len is {}\n".format(range(len(phrase_potential))))

for i in range(len(phrase_potential)):
    for j in range(i+1,6):
        for sentence in x:
            print("i,j,sentence are {},{},{}".format(phrase_potential[i], phrase_potential[j], sentence))
            if phrase_potential[i] in sentence and phrase_potential[j] in sentence[i:]:
                phrase_pool.append(phrase_potential[i]+phrase_potential[j])
            

# for 3 letters
'''
for word1 in phrase_potential:
    for word2 in phrase_potential[word1:]:
        for word3 in phrase_potential[word2:]:
            phrase_pool.append(str(word1)+str(word2)+str(word3))
'''


phrase_pool_unique = list(set(phrase_pool))
print("phrase_pool_unique is {}".format(phrase_pool_unique))

phrase_final = {}

for i in phrase_pool_unique:
    if phrase_pool.count(i) > 1:
        phrase_final[i]=phrase_pool.count(i)
print("phrase_final is {}".format(phrase_final))
    

'''
#------------------------- need to update
#3 check if the data in phrase_pool are really phrases

phrase_time = {}
phrase = []
for phrase in phrase_pool:
    for sentence in x:
        if phrase in sentence:
            appear_times += 1
    phrase_time[phrase] = appear_times
    if appear_times > 1:
        phrase.append(phrase)
    appear_times = 0

print("the phrase are {}, and the time they appeared are {}".format(phrase,phrase_time))
'''
