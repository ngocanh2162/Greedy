import re
import setting
import convert

def get_syll_init_list():
    with open("../data/syllable/syll_init.txt") as sylls:
        sylls_arr = []
        for line in sylls:
            sylls_arr += line.split(", ")
        return sylls_arr

# segment syll vietnamese
def syll_seg(word):
    dict_telex_tone = convert.read_map_charater(setting.PATH_TELEX_TONE)

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

# normalize word wrong accent
# example : húê -> huế

def normalized_accent(word):

    map_telex = convert.read_map_telex(setting.PATH_TELEX_TONE)
    syll_init, medial, princ_vowel, final_sound, tone = syll_seg(word)
    word_accent = ""
    final_sound_arr = ['p', 't', 'c', 'ch', 'm', 'n', 'ng', 'nh', 'o', 'u', 'i']
    voewl_1 = ['iê', 'yê', 'uô', 'ươ']
    voewl_2 = ['ia', 'ya', 'ua', 'ưa']
    if len(princ_vowel) == 1:
        if medial != '' and final_sound == '':
            final_sound = princ_vowel
            princ_vowel = medial
            medial = ''
        if tone != '':
            char_tone = princ_vowel + "_" + tone
            princ_vowel = map_telex[char_tone]
        word_accent = syll_init + medial + princ_vowel + final_sound
    elif princ_vowel in voewl_1 and final_sound in final_sound_arr:
        first_voewl, second_voewl = princ_vowel[0], princ_vowel[1]
        if tone != '':
            char_tone = second_voewl + "_" + tone
            princ_vowel = first_voewl + map_telex[char_tone]
        word_accent = syll_init + medial + princ_vowel + final_sound
    elif princ_vowel == 'ia':
        if syll_init == 'g':
            first_voewl, second_voewl = princ_vowel[0], princ_vowel[1]
            if tone != '':
                char_tone = second_voewl + "_" + tone
                princ_vowel = first_voewl + map_telex[char_tone]
            word_accent = syll_init + medial + princ_vowel + final_sound
        else:
            first_voewl, second_voewl = princ_vowel[0], princ_vowel[1]
            if tone != '':
                char_tone = first_voewl + "_" + tone
                princ_vowel = map_telex[char_tone] + second_voewl
            word_accent = syll_init + medial + princ_vowel + final_sound
    elif princ_vowel == 'ua':
        if syll_init == 'q':
            first_voewl, second_voewl = princ_vowel[0], princ_vowel[1]
            if tone != '':
                char_tone = second_voewl + "_" + tone
                princ_vowel = first_voewl + map_telex[char_tone]
            word_accent = syll_init + medial + princ_vowel + final_sound
        else:
            first_voewl, second_voewl = princ_vowel[0], princ_vowel[1]
            if tone != '':
                char_tone = first_voewl + "_" + tone
                princ_vowel = map_telex[char_tone] + second_voewl
            word_accent = syll_init + medial + princ_vowel + final_sound
    elif princ_vowel in voewl_2:
        first_voewl, second_voewl = princ_vowel[0], princ_vowel[1]
        if tone != '':
            char_tone = first_voewl + "_" + tone
            princ_vowel = map_telex[char_tone] + second_voewl
        word_accent = syll_init + medial + princ_vowel + final_sound

    return word_accent

# convert telex style to word utf-8
# example : huees -> huế
def telex_to_word(word_telex):
    word_re_telex = convert.syll_replace_telex(word_telex)
    word = normalized_accent(word_re_telex)
    return word


# word_test = "khuynh"
# word_telex = convert.syll_to_telex(word_test)
# print(word_telex)
# print(telex_to_word("toongs"))
# print(syll_seg('an'))
