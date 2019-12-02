import matplotlib.pyplot as plt
import numpy as np
import  pickle

def visualize(x, y, labels, high, x_name, y_name):
    plt.bar(x, np.divide(list(y), sum(y)), label = labels)
    plt.ylim(0,high)
    plt.ylabel (y_name)
    plt.xlabel (x_name)
    plt.xticks(list(x))
    plt.legend (bbox_to_anchor=(1, 1), loc="upper right", borderaxespad= 0., labelspacing=0.5)
    plt.show()

len_sentences = pickle.load(open("data/len_sen.pkl", "rb"))
x = ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','>100']
keys = x
vals = list(len_sentences.values())[0:21]
visualize(keys, vals, "", 0.15, "x", "y")