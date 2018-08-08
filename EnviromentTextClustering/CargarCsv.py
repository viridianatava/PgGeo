#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:15:03 2018

@author: roberto
"""
import pandas as pd
#path and name of the file
fileName='./muestra2.csv'

df = pd.read_csv(fileName, thousands=',')
print(df)