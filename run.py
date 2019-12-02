import greedy
import pre
import setting


temp1 = pre.readFile(setting.PATH_TARGET_LIST)
# temp2 = pre.readFile(setting.PATH_TARGET_NSW)
syDict = pre.readFile(setting.PATH_6000_SYLLABLES)
NSWDict = {'NTIM': 0, 'NDAT': 0, 'NDAY': 0, 'NMON': 0, 'NNUM': 0, 'NTEL': 0, 'NDIG': 0, 'NRNG': 0, 'NPER': 0, 
           'NFRC': 0, 'NADD': 0, 'LWRD': 0, 'LSEQ': 0, 'LABB': 0, 'PUNC': 0, 'URLE': 0, 'MONY': 0, 'DURA': 0,
           'NSCR': 0, 'CSEQ': 0, 'NONE': 0}
# NSWDict = {'ph': 0, 'th': 0, 'tr': 0, 'd': 0, 'gi': 0, 'ch': 0, 'nh': 0, 'ng': 0, 
#             'ngh': 0, 'kh': 0, 'g': 0, 'gh': 0, 'c': 0, 'q': 0, 'k': 0, 't': 0, 
#             'r': 0, 'h': 0, 'b': 0, 'm': 0, 'v': 0, 'đ': 0, 'n': 0, 'l': 0, 'x': 0,
#             'p': 0, 's': 0, 'i': 0, 'y': 0, 'ê': 0, 'e': 0, 'a': 0, 'ă': 0, 'ơ': 0, 
#             'â': 0, 'ư': 0, 'ô': 0, 'oo': 0, 'o': 0, 'u': 0, 'ia': 0, 'ya': 0, 'iê': 0, 
#             'yê': 0, 'uô': 0, 'ua': 0, 'ươ': 0, 'ưa': 0, 'zero': 0}
for para in temp1:
    for word in para.split():
        if word in syDict:
            syDict[word] += 1
# for para in temp2:
#     for NSW, q in para.items():
# #         NSWDict[NSW] += q

A, B = greedy.greedy(setting.PATH_SOURCE_PARA, setting.PATH_SOURCE_NSW, setting.PATH_TARGET_LIST, setting.PATH_COUNT_NSW, syDict, NSWDict)