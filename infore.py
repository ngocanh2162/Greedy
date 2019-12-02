import csv
import pickle
import pre

# text_list = []
# csv.register_dialect('myDialect', delimiter = '|', quoting=csv.QUOTE_ALL, skipinitialspace=True)
# with open('/content/drive/My Drive/data/metadata.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile, dialect='myDialect')
#     for row in reader:
#       text_list.append(row[1])
# csvFile.close()
# pre.saveFile(text_list, 'data/infore_text.pkl')
text_list = pre.readFile('data/infore_text.pkl')

# thống kê độ dài câu, độ phủ âm tiết, âm vị
len_sentences = dict.fromkeys(range(8),0)
syDict = pickle.load(open('data/syllables.pkl',"rb"))
phoneDict = {'ph': 0, 'th': 0, 'tr': 0, 'd': 0, 'gi': 0, 'ch': 0, 'nh': 0, 'ng': 0, 
            'ngh': 0, 'kh': 0, 'g': 0, 'gh': 0, 'c': 0, 'q': 0, 'k': 0, 't': 0, 
            'r': 0, 'h': 0, 'b': 0, 'm': 0, 'v': 0, 'đ': 0, 'n': 0, 'l': 0, 'x': 0,
            'p': 0, 's': 0, 'i': 0, 'y': 0, 'ê': 0, 'e': 0, 'a': 0, 'ă': 0, 'ơ': 0, 
            'â': 0, 'ư': 0, 'ô': 0, 'oo': 0, 'o': 0, 'u': 0, 'ia': 0, 'ya': 0, 'iê': 0, 
            'yê': 0, 'uô': 0, 'ua': 0, 'ươ': 0, 'ưa': 0, 'zero': 0}
for para in text_list:
  sentence = para.split()
  for syll in sentence:
    if syll in syDict:
      syDict[syll] += 1
    word = pre.syll_seg(syll)
    for j in range(4): 
      if word[j] in phoneDict:
        if word[j] != '':
          phoneDict[word[j]] += 1
        else:
          phoneDict['zero'] +=1
  len_sentences[int(len(sentence)/5)]  += 1
pre.saveFile(syDict, 'data/infore_syDict.pkl')

# print(phoneDict)
# print(syDict)
# temp = []
# for sy, count in syDict.items():
#   if count == 0:
#     temp.append(sy)
# print(len(temp))