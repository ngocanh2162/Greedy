import greedy
import setting
import pre
import re

import glob
dirX = glob.glob("/content/drive/My Drive/new_result/X/***.pkl")
file_path_X = "/content/drive/My Drive/new_result/X/"
file_path_Y = "/content/drive/My Drive/new_result/Y/"
pre.saveFile([], setting.PATH_SOURCE_PARA)
pre.saveFile([], setting.PATH_SOURCE_NSW)
pre.saveFile([], setting.PATH_TARGET_LIST)
pre.saveFile([], setting.PATH_TARGET_NSW)
for datafile in dirX:
  codename = datafile[-12:-4]
  source_List = pre.readFile(setting.PATH_SOURCE_PARA)
  # source_NSW_counter = pre.readFile(setting.PATH_SOURCE_NSW)
  Xtemp = pre.readFile(file_path_X + 'x' + codename + '.pkl')
  # Ytemp = pre.readFile(file_path_Y + 'y' + codename + '.pkl')
  key_temp = []
  for i in range(len(Xtemp)-1):
    temp = re.sub('\.|\,|\;|\!|\?', '', Xtemp[i])
    if len(temp.split()) < 50 or len(temp.split()) > 350 :
      key_temp.append(i)
  key_temp.reverse()
  for j in key_temp:
      del Xtemp[j]
      # del Ytemp[j]
  source_List.extend(Xtemp)
  pre.saveFile(source_List, setting.PATH_SOURCE_PARA)
  # source_NSW_counter.extend(Ytemp)
  # pre.saveFile(source_NSW_counter, setting.PATH_SOURCE_NSW)
  print("doneX", codename, len(Xtemp), len(source_List))
  del source_List[:]
  # del source_NSW_counter[:]