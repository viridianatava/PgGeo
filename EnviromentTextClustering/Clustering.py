#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import re
from sklearn.feature_extraction.text import TfidfVectorizer
#Machine learning
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
 

from gensim import corpora
import gensim    

import csv



def tokenize(text):
    min_length = 3
    
    words = map(lambda word: word.lower(), word_tokenize(text))
    words = [word for word in words if word not in (StopWordsList or stopWord_p)]
    tokens = (list(map(lambda token: stemmer.stem(token), words)))
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = list(
        filter(lambda token: p.match(token) and len(token) >= min_length,
               tokens))
    return filtered_tokens

def represent(documents):
    # Tokenisation
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    # Learn and transform train documents
    vectorised_documents = vectorizer.fit_transform(documents)
    
    return vectorised_documents
#path and name of the file
pathCsvfileInput='./muestra.csv'
pathCsvfileOutput1="./clustersResults1.csv"
pathCsvfileOutput2="./clustersResults2.csv"


print("------------------------------------------------------")
print("#################  Reading CSV file #####")
#Read the file and drop the nan values
data = pd.read_csv(pathCsvfileInput, thousands=',',  header=None, error_bad_lines=False)
print(data.shape)
 

publicacion_doc= data.iloc[:,0].dropna(how='any')
pub_doc=[element for element in publicacion_doc]

print(type(publicacion_doc))

print("------------------------------------------------------")
print("#################  Running stopwords cleansing  #####")
print("------------------------------------------------------")


StopWordsList = stopwords.words("spanish")
stopWord_p=["tiempo","tabasco","tabascohoy","alertath","http","https","preview=true","eluniversal","lacapital","quenosetep","hayquesab"]

stemmer = SnowballStemmer("spanish")

print("------------------------------------------------------")
print("####  Running vectorized model, #Files and #Columns ##")
print("------------------------------------------------------")
vectorised_publication=represent(pub_doc)
svd = TruncatedSVD(n_components=100, n_iter=7, random_state=42)
normalizer = Normalizer(copy=False)
lsa = make_pipeline(svd, normalizer)

print("------------------------------------------------------")
print("#################  Running LSA model  #####")

X = lsa.fit_transform(vectorised_publication)
#

print("----------------------------------------------------------")
print("########## Starting Big K-means Clustering model   #######")
print("----------------------------------------------------------")

n_clusters=50
KM=KMeans(n_clusters=n_clusters).fit(X)
labels_KM = KM.labels_
clusters={}
iteration=0
for element in labels_KM:
    if element not in clusters:
        list_prov=[]
        list_prov.append(pub_doc[iteration])
        clusters[element]=list_prov
    else:
        prov=clusters[element]
        prov.append(pub_doc[iteration])
        clusters[element]=prov
    iteration+=1 
   
print("----------------------------------------------------------")
print("######## Clustering results before LDA   #################")
print("----------------------------------------------------------")


with open(pathCsvfileOutput1, 'w', encoding='utf-16', newline='') as csvFile:
    fieldnames = ['idC','texts']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames) 
    writer.writeheader()   
    for element in clusters:
        writer.writerow({'idC':element, 'texts':clusters[element]})

print("----------------------------------------------------------")
print("################# Starting LDA model   ###################")
print("----------------------------------------------------------")
for element in clusters:
    texts=[tokenize(text) for text in clusters[element]]
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]
    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
    print("----------------------------------------------------------")
    print("######## Clustering topics results after LDA   ##################")
    print("----------------------------------------------------------")
    print(ldamodel.print_topics(num_topics=1, num_words=10))













## #############################################################################
# Compute Affinity Propagation
#af = AffinityPropagation(preference=-5,verbose='True').fit(X)
#cluster_centers_indices = af.cluster_centers_indices_
#labels_af = af.labels_

#n_clusters_ = len(cluster_centers_indices)
##
## #############################################################################
## Compute DBSCAN
#db = DBSCAN(eps=0.01, min_samples=20,n_jobs=-1)
#results=db.fit_predict(X)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
#labels_db = db.labels_


    

