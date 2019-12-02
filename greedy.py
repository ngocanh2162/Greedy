import datetime
import pre
import setting
import re

def score(syScore, NSWscore, L):
    return float(syScore*2 + NSWscore)/float(L)

def calScore(source_corpus_List, source_NSW_List, syllable_Dict, NSW_Dict):
    paragraph_score_dict, new_word_score_dict = {}, {}
    for i in range(len(source_corpus_List)):
        paragraph = re.sub('\.|\,|\;|\!|\?', '', source_corpus_List[i])
        paragraph = paragraph.split()
        paragraph_distint = {x:paragraph.count(x) for x in paragraph}
        L = len(paragraph_distint) 
        syScore = 0
        new_word_count = 0
        for word, count in paragraph_distint.items():
            if word in syllable_Dict:
              if syllable_Dict[word] == 0:
                new_word_count +=1
              if syllable_Dict[word] < setting.N1:
                syScore += min(count, setting.N1 - syllable_Dict[word])
              else:
                syScore += -1
        NSWscore = 0
        # for NSW, q in source_NSW_List[i].items():
        #     if NSW_Dict[NSW] < N2:
        #         NSWscore += min(q, N2 - NSW_Dict[NSW])
        #     else:
        #         NSWscore += -min(q, NSW_Dict[NSW]-N2)
        #         # NSWscore += -1
        #     if NSW_Dict[NSW] == 0:
        #         new_word_count +=1
        new_word_score_dict[i] = new_word_count
        paragraph_score_dict[i] = score(syScore, NSWscore, L)
    have_max_new_word = max(new_word_score_dict, key = new_word_score_dict.get)
    if new_word_score_dict[have_max_new_word] <= 1:
          return -1
    best_paragraph_index = max(paragraph_score_dict, key = paragraph_score_dict.get)
    print(new_word_score_dict[have_max_new_word], paragraph_score_dict[best_paragraph_index])
    if paragraph_score_dict[best_paragraph_index] < 0:
         best_paragraph_index = have_max_new_word
    paragraph_score_dict.clear()
    new_word_score_dict.clear()
    return best_paragraph_index

# NSW_Dict maybe is phone_Dict
def greedy_selection(source_file, source_NSW_file, target_file, target_NSW_file, syllable_Dict, NSW_Dict, flag):
    source_corpus_List = pre.readFile(source_file)
    source_NSW_List = pre.readFile(source_NSW_file)
    target_List = pre.readFile(target_file)
    target_NSW_List = pre.readFile(target_NSW_file)
    best_paragraph_index = calScore(source_corpus_List, source_NSW_List, syllable_Dict, NSW_Dict)
    if best_paragraph_index == -1:
        print("Ko the phu them am tiet")
        return source_file, source_NSW_file, target_file, target_NSW_file, syllable_Dict, NSW_Dict, False
    target_List.append(source_corpus_List[best_paragraph_index])
    # target_NSW_List.append(source_NSW_List[best_paragraph_index])
    for word in source_corpus_List[best_paragraph_index].split():
        if word in syllable_Dict:
            syllable_Dict[word] += 1
    # for NSW, q in source_NSW_List[best_paragraph_index].items():
    #         NSW_Dict[NSW] += q
    del source_corpus_List[best_paragraph_index]
    # del source_NSW_List[best_paragraph_index]
    if len(source_corpus_List) == 0:
        print("Het data de chon")
        return source_file, source_NSW_file, target_file, target_NSW_file, syllable_Dict, NSW_Dict, False
    pre.saveFile(source_corpus_List, source_file)
    # pre.saveFile(source_NSW_List, source_NSW_file)
    pre.saveFile(target_List, target_file)
    pre.saveFile(target_NSW_List, target_NSW_file)
    print(len(source_corpus_List), len(target_List))
    del source_corpus_List[:]
    # del source_NSW_List[:]
    del target_List[:]
    del target_NSW_List[:]
    return source_file, source_NSW_file, target_file, target_NSW_file, syllable_Dict, NSW_Dict, True

def greedy(source_file, source_NSW_file, target_file, target_NSW_file, syllable_Dict,NSW_Dict):
    i = 0
    flag = True
    while (True):
        i += 1
        ts = datetime.datetime.now()
        source_file, source_NSW_file, target_file, target_NSW_file, syllable_Dict, NSW_Dict, flag = greedy_selection(source_file, source_NSW_file, target_file, target_NSW_file, syllable_Dict, NSW_Dict, flag)
        tf = datetime.datetime.now()
        print(i, tf-ts)
        if flag == False:
            break
    return syllable_Dict, NSW_Dict