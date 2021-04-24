# -*- coding: utf-8 -*-
"""
Generates word from trigramm transition matrix stored in a binary file
Checks whether the word already exists
"""

import numpy as np
from numpy.random import choice
import codecs

# Build a dictionnary to check whether word already exists
filepath = "liste.de.mots.francais.frgut.txt"
dico = []
with codecs.open(filepath, "r", "utf-8") as lines:
    for l in  lines:
        dico.append(l[:-1])
 
# Load the trigram count matrixand normalize it     
count = np.fromfile("count2D.bin",dtype="int32").reshape(256,256,256)
s=count.sum(axis=2)
st=np.tile(s.T,(256,1,1)).T
p=count.astype('float')/st
p[np.isnan(p)]=0


# Build words
outfile = "output.txt"
f = codecs.open(outfile,"w","utf-8")

# How many for each target size
K = 100
for TGT in range(4,11):
    total = 0
    while total<100:
        i=0
        j=0
        res = u''
        while not j==10:
            k=choice(range(256),1,p=p[i,j,:])[0]
            res = res + chr(k)
            i=j
            j=k
        if len(res) == 1+TGT:
            if res[:-1] in dico:
                x=res[:-1]+"*"
            else:
                x=res[:-1]
            total += 1
            print(x)
            f.write(x+"\n")
f.close()