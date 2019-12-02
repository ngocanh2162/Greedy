import re
from nltk.tokenize import sent_tokenize
import pre

# 1. get source 
import glob
dirX = glob.glob("/content/drive/My Drive/new_result/X/***.pkl")
file_path_X = "/content/drive/My Drive/new_result/X/"
pre.saveFile([], 'data/source2.pkl')
for datafile in dirX:
    codename = datafile[-12:-4]
#   if codename not in ["_2019_11","_2019_10","_2019_09","_2019_08","_2019_07","_2019_06",]:
    source_List = pre.readFile('data/source2.pkl')
    Xtemp = pre.readFile(file_path_X + 'x' + codename + '.pkl')
    source_List.extend(Xtemp)
    pre.saveFile(source_List, 'data/source2.pkl')
    print("doneX", codename, len(Xtemp), len(source_List))
    del source_List[:]
    del Xtemp[:]

# 2.1. source -> sentences, syllables coverages
source_list = pre.readFile('data/source2.pkl')
sentences = []
for para in source_list:
  t = sent_tokenize(para)
  sentences.extend(t)
pre.saveFile(sentences, 'data/source2.pkl')
print('Chua', len(sentences), 'cau')
del source_list[:]

syDict2 = pre.readFile('data/syllables.pkl')
pre.saveFile(syDict2, 'data/syllables2.pkl')
len_sen = dict.fromkeys(range(200),0)
pre.saveFile(len_sen, 'data/len_sen.pkl')

# 2.2. tính độ dài câu
sentences = pre.readFile('data/source2.pkl')
syDict2 = pre.readFile('data/syllables2.pkl')
len_sentences = pre.readFile('data/len_sen.pkl')

count_sen = len(sentences)
for i in range(len(sentences)):
  sentence = re.sub('\.|\,|\;|\!|\?', '', sentences[i]).split()
  if 0 < len(sentence):
    if len(sentence) < 200:
      len_sentences[int(len(sentence)/5)]  += 1
  else: 
    count_sen -= 1
  for word in sentence:
    if word in syDict2:
      syDict2[word] += 1
pre.saveFile(len_sentences, 'data/len_sen.pkl')
pre.saveFile(syDict2, 'data/syllables2.pkl')
del sentences[:]

print('Trong', count_sen, 'câu')
c = []
for sy, count in syDict2.items():
  if count == 0:
    c.append(sy)
print('Phủ', len(syDict2) - len(c),'trên', len(syDict2), 'âm tiết thường gặp')

# 3. get diphone
dirX = glob.glob("/content/drive/My Drive/new_result/X/***.pkl")
file_path_X = "/content/drive/My Drive/new_result/X/"
for datafile in dirX:
    codename = datafile[-12:-4]
  # if codename not in ["_2019_11","_2019_10","_2019_09","_2019_08","_2019_07","_2019_06",]:
    diphone = pre.readFile('data/diphone.pkl')
    Xtemp = pre.readFile(file_path_X + 'x' + codename + '.pkl')
    for para in Xtemp:
        para = re.sub('\.|\,|\;|\!|\?', '', para)
        sylls = para.split()
        for word in sylls:
            di_phone = pre.di_seg(word)
            diphone = diphone.union(set(di_phone))
    pre.saveFile(diphone, 'data/diphone.pkl')
    print("doneX", codename, len(diphone))
    del Xtemp[:]