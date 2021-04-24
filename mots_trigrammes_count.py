# -*- coding: utf-8 -*-

# Count the occurence of ASCII characters trigrams in a text file

import os
import numpy as np

import codecs


for suffix in ('fr','en'):
    count = np.zeros((256,256,256),dtype='int32')
    res = []
    with codecs.open("words_"+suffix+".txt", "r", "utf-8") as lines:
        for l in  lines:
            i=0
            j=0
            for k in [ord(c) for c in list(l)]:
                count[i,j,k] += 1
                i = j
                j = k
    count.tofile("count_"+suffix+".bin")
