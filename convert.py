import setting

# get map of utf-8 character to telex
# example : đ - dd

def read_map_charater(file):
    dict_telex = {}
    f =  open(file, 'r', encoding="utf8")
    content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(len(content)):
        temp = content[i].split("-")
        dict_telex[temp[0]] = temp[1]
    return dict_telex

# get map of telex character to utf-8
# example : dd - đ

def read_map_telex(file):
    dict_telex = {}
    f =  open(file, 'r', encoding="utf8")
    content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(len(content)):
        temp = content[i].split("-")
        dict_telex[temp[1]] = temp[0]
    return dict_telex

# get list of telex character
# example : â, ô, ...

def get_list_telex_character(file):
    list_telex_character = []
    f =  open(file, 'r', encoding="utf8")
    content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(len(content)):
        temp = content[i].split("-")
        list_telex_character.append(temp[1])
    return list_telex_character

# get list of telex tone
# example : j, s, ...

def get_list_telex_tone(file):
    list_telex_tone = []
    f =  open(file, 'r', encoding="utf8")
    content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(len(content)):
        temp = content[i].split("_")
        if temp[1] not in list_telex_tone:
            list_telex_tone.append(temp[1])
    return list_telex_tone

# convert utf-8 syll to telex type
# example : như -> nhuw

def syll_to_telex(word):
    dict_telex = read_map_charater(setting.PATH_TELEX_CHAR)
    dict_telex_tone = read_map_charater(setting.PATH_TELEX_TONE)

    for k, v in dict_telex_tone.items():
        if k in word:
            character, tone = v.split("_")[0], v.split("_")[1]
            word = word.replace(k, character)
            word = word + tone

    for k, v in dict_telex.items():
        if k in word:
            word = word.replace(k, v)
    return word

# extract syll to syll + tone
# example : việt -> viêtj
def syll_extract_tone(word):
    dict_telex_tone = read_map_charater(setting.PATH_TELEX_TONE)

    for k, v in dict_telex_tone.items():
        if k in word:
            character, tone = v.split("_")[0], v.split("_")[1]
            word = word.replace(k, character)
            word = word + tone

    return word

# replace telex character to utf-8 character
# example : aa -> â
def syll_replace_telex(word_telex):
    dict_telex = read_map_charater(setting.PATH_TELEX_CHAR)
    for k, v in dict_telex.items():
        if v in word_telex:
            word_telex = word_telex.replace(v, k)
    return word_telex

def str_to_telex(str):
    words = str.split(" ")
    telex_str = ""
    for i in range(len(words)):
        words[i] = syll_to_telex(words[i])
        if i != len(words) - 1:
            telex_str += words[i] + " "
        else:
            telex_str += words[i]
    return telex_str

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
