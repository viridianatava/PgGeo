# -*- coding: utf-8 -*-
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from time import time
import numpy as np



################################################################################
########## Recuperacion de clases, conjunto de entrenamiento, bolsa de palabras 
################################################################################
print("----------------------------------")
print("Cargando archivos...")
tiempo0 = time()
x_setEntrenamientoTweets = [line.rstrip('\n') for line in open('dataTraining.txt')]
y_clases = [line.rstrip('\n') for line in open('clases.txt')]
bolsaDePalabras = [line.rstrip('\n') for line in open('bagOfWords2.txt')]
x_setTesting = [line.rstrip('\n') for line in open('dataTesting.txt')]

tiempoFinal = time() - tiempo0
print("Se cargaron datos de clasificación en: " + str(tiempoFinal))

################################################################################
########## Vectorizacion                                              ##########
################################################################################
print("----------------------------------")
print("\n Creando la representacion numerica (vectorizando tweets)")
tiempo0 = time()
# max_features : int or None, default=None
#If not None, build a vocabulary that only consider the top max_features
# ordered by term frequency across the corpus.
# This parameter is ignored if vocabulary is not None.
vectorizador = TfidfVectorizer(max_features=54)
#vectorizador = TfidfVectorizer(max_features=74)
#TfidfVectorizer: Convert a collection of raw documents to a matrix of TF-IDF features.
vectorizador.fit(bolsaDePalabras)
#fit(raw_documents[, y])	Learn vocabulary and idf from training set.
x_matrizSetEntrenamientoVect = vectorizador.fit_transform(x_setEntrenamientoTweets)

#Learn vocabulary and idf, return term-document matrix.
#This is equivalent to fit followed by transform, but more efficiently implemented.
#Parameters:	raw_documents : iterable
#an iterable which yields either str, unicode or file objects
#Returns:	
#X : sparse matrix, [n_samples, n_features]
#Tf-idf-weighted document-term matrix.

print (x_matrizSetEntrenamientoVect);
#transform(raw_documents, copy=True)[source]. 
#Uses the vocabulary and document frequencies (df) learned by fit (or fit_transform).
x_matrizPrueba = vectorizador.transform(x_setTesting)
#matrizVectorizada = np.array(matrizVectorizada, dtype='float_')
tiempoFinal = time() - tiempo0
print("Se ha creado la matriz TF-IDF en "+format(tiempoFinal))
print("----------------------------------")

################################################################################
########## Clasificacion
################################################################################

################################################################################
########## Bayes multinomial
################################################################################
print("----------------------------------")
print("Traning con clasificador MultinomialNB  bayes: ")
t0 = time()
multinomialBY = MultinomialNB()
#clf.fit(matrizVectorizada, tweetsClases)

multinomialBY.fit(x_matrizSetEntrenamientoVect, y_clases)

print("Testing: clasificador bayesiano...")
t0 = time()
res1 = multinomialBY.predict(x_matrizPrueba)
scores = cross_val_score(multinomialBY, x_matrizSetEntrenamientoVect, y_clases, cv = 10)

print (np.mean(scores))
tiempoFinal = time() - tiempo0


print("Termino en "+format(tiempoFinal))
print("----------------------------------")

################################################################################
# Support Vector Machine
################################################################################
print("----------------------------------")
print(" Traning con clasificador SVM sin parametros")
t0 = time()
svm = SVC()
#clf.fit(matrizVectorizada, tweetsClases)
scores = cross_val_score(svm, x_matrizSetEntrenamientoVect, y_clases, cv = 10)

print (np.mean(scores))
svm.fit(x_matrizSetEntrenamientoVect, y_clases)
print("Temino en {0} s".format(time() - t0))
print("Probando clasificador SVC...")
t0 = time()
res2 = svm.predict(x_matrizPrueba)
t1 = time() - t0
tiempoFinal = time() - tiempo0


print("Temino en {0} segundos SVM sin parametros".format(tiempoFinal))
print("----------------------------------")

print("----------------------------------")
print(" Traning con clasificador SVM : C= 1.0, gamma=0.10000000000000001 ")
t0 = time()
rbf_svc = SVC(kernel='rbf', C= 1.0, gamma=0.10000000000000001)
#clf.fit(matrizVectorizada, tweetsClases)
scores = cross_val_score(rbf_svc, x_matrizSetEntrenamientoVect, y_clases, cv = 10)
t1 = time() - t0
print (np.mean(scores))
rbf_svc.fit(x_matrizSetEntrenamientoVect, y_clases)
print("Temino en"+format(t1))
print("Probando clasificador SVC...")
t0 = time()
res3 = rbf_svc.predict(x_matrizPrueba)
tiempoFinal = time() - tiempo0


print("Temino en {0} segundos".format(tiempoFinal))
print("----------------------------------")

################################################################################
#
#    Estimacion de paramatros para SVM
#
#################################################################################
print("Estimacion de paramatros para SVM RBF con GridSearchCV")
parametersSVM = {"C":  [1,10,100, 1000, 10000,100000],
              "gamma": [0.1,0.01,0.001,0.0001,1,10,100]}

gs_clf = GridSearchCV(rbf_svc, parametersSVM, n_jobs=-1)
gs_clf = gs_clf.fit(x_matrizSetEntrenamientoVect,y_clases)
gs_clf.best_score_ 

rbf_svc_tunning = gs_clf.best_estimator_

#y_clases.target_names[gs_clf.predict(['La contaminacion del aire debe ser de muchos imecas se siente en el aire'])[0]]
for param_name in sorted(parametersSVM.keys()):
    print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))

y_svm2 = rbf_svc_tunning.fit(x_matrizSetEntrenamientoVect, y_clases)
res4=rbf_svc_tunning.predict(x_matrizSetEntrenamientoVect)

print(x_matrizSetEntrenamientoVect)
training=1
for labes in res4:
    print ("Texto num["+ format(training)+"]- "+labes)
    training=training+1

score1=rbf_svc_tunning.score(x_matrizSetEntrenamientoVect, y_clases)
print (np.mean(score1))



print("----------------------------------")


################################################################################
# Persistentencia
################################################################################
print("----------------------------------")
print("\n Guardando en disco del entrenamiento...")
time0 = time()
print (rbf_svc_tunning.score(x_matrizSetEntrenamientoVect, y_clases))
joblib.dump(vectorizador, 'matVectorizador.dat')
joblib.dump(rbf_svc_tunning, 'clasificadorModelEntrenado.dat')
tiempoFinal = time() - tiempo0
print("Finalizo en " + str(tiempoFinal))
################################################################################
