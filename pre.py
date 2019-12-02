import re
import pickle
import setting

def read_map_charater(file):
    dict_telex = {}
    f =  open(file, 'r', encoding="utf8")
    content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(len(content)):
        temp = content[i].split("-")
        dict_telex[temp[0]] = temp[1]
    return dict_telex

def syll_seg(word):
    dict_telex_tone = read_map_charater(setting.PATH_TELEX_TONE)

    # extract syll + tone
    # example : huế -> huês
    for k, v in dict_telex_tone.items():
        if k in word:
            character, tone = v.split("_")[0], v.split("_")[1]
            word = word.replace(k, character)
            word = word + tone

    m = re.match(r'(b|c|d|đ|g|h|k|l|m|n|p|q|r|s|t|v|x|)(g|h|i|r|)(h|)(o|u|)(a|ă|â|e|ê|i|o|ô|ơ|u|ư|y)(a|ê|ô|ơ|)(c|i|m|n|o|p|t|u|y|)(h|g|)(f|s|r|x|j|)', word)
    if m == None:
        return '', '', '', '', ''

    syll_init, medial, princ_vowel, final_sound, tone = m.group(1) + m.group(2) + m.group(3), m.group(4), m.group(5) + m.group(6), m.group(7) + m.group(8), m.group(9)
    if medial == 'u' and ( princ_vowel == 'a' or princ_vowel == 'ô'):
        princ_vowel = medial + princ_vowel
        medial = ''
    if m.group(2) == 'i' and (m.group(5) == 'a' or m.group(5) == 'ê'):
        syll_init = m.group(1) + m.group(3)
        princ_vowel = 'i' + m.group(5)
    return syll_init, medial, princ_vowel, final_sound, tone

def di_seg(word):
    syll = syll_seg(word)
    return syll[0] + syll[1], syll[1] + syll[2],syll[2] + syll[3]

def saveFile(item, filePath):
    with open(filePath, 'wb') as fp:
        pickle.dump(item, fp)

def readFile(filePath):
    try:
        item = pickle.load(open(filePath,"rb"))
    except EOFError:
        item = []
    return item
