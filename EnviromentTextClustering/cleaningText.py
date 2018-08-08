#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 00:13:05 2018

@author: roberto
"""

# coding=utf-8

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import unicodedata

 

def CleansingText(text):
    print(type(text))
    text = unicodedata.normalize('NFD', text.decode('utf-8')).encode('ascii', 'ignore').decode('utf-8')
    stop = set(stopwords.words('spanish'))
   
    
    punct = set(['“','”','!','"','#','$','%','&','/','(',')','=','?','¿','*','[',']','{','}','-','_','*','¡','.',':',';',',','^','>','<','@','...','+',"'", ' ', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z'])
    stop.update(['rt'])
    
    
    stop.remove('no')
    stop.remove('ni')
    stop.remove('sin')
    stop.remove('mucho')
    stop.remove('muchos')
    stop.remove('todos')
    stop.remove('contra')
 
    stemmer = SnowballStemmer("spanish")
    wstopText = []
    wstopText2 =[]
    wStopList = []

   # text = unicodedata.normalize('NFD', decode('utf-8')).encode('ascii', 'ignore').decode('utf-8')
    text = text.lower()

    for word in text.split():
        if word not in stop and 'http' not in word and 'https' not in word and word not in punct:
            wstopText.append(word)
    
    toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
    wstopText = toker.tokenize(' '.join(wstopText))

    for word in wstopText:
        if word not in punct:
            wstopText2.append(word)

    for word in wstopText2:
        wstopText2 = [stemmer.stem(s) for s in wstopText2]
        wStopList.append(' '.join(wstopText2))
        break

    if len(wStopList):
        return wStopList
    return ''

print(preprocessing("- https http rt MONTERREY TUVO OTRO AÑO PERDIDO EN EL COMBATE A LA CONTAMINACIÓN - Me sumo a la iniciativa #respiramonterrey par… https://t.co/mR28K81VIW"))