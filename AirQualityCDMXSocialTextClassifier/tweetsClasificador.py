# -*- coding: utf-8 -*-

from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import  make_scorer
from sklearn.model_selection import GridSearchCV
from matplotlib.pylab import hist, show, plt
import re
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from time import time
import numpy as np

def getDistribucionClases(clasesPath):
    frequency = {}
    document_text = open(clasesPath, 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'b[a-z]{2,15}b', text_string) 
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1    
    frequency_list = frequency.keys() 
    for words in frequency_list:
        print words, frequency[words]
    return frequency



#Títulos para las gráficas
titles = ['SVC','SVC RBF kernel','SVC RBF tuning∫']

def getGraph():
    for i, clf in enumerate((svm, rbf_svc, rbf_svc_tunning)):
     # Se grafican las fronteras 
     plt.subplot(2, 2, i + 1)
     plt.subplots_adjust(wspace=0.4, hspace=0.4)
    
     Z = clf.predict(np.c_[x_matrizSetEntrenamientoVect, y_clases])
    
     #Color en las gráficas
     Z = Z.reshape(x_matrizSetEntrenamientoVect.shape)
     plt.contourf(x_matrizSetEntrenamientoVect, y_clases, Z, cmap=plt.cm.Paired, alpha=0.8)
    
     #Puntos de entrenamiento
     plt.scatter(x_matrizSetEntrenamientoVect[:, 0], x_matrizSetEntrenamientoVect[:, 1], c=y_clases, cmap=plt.cm.Paired)
     plt.xlabel('Longitud Sepal')
     plt.ylabel('Peso Sepal')
     plt.xlim(x_matrizSetEntrenamientoVect.min(), x_matrizSetEntrenamientoVect.max())
     plt.ylim(y_clases.min(), y_clases.max())
     plt.xticks(())
     plt.yticks(())
     plt.title(titles[i])
    
    plt.show()
################################################################################
########## Recuperacion de clases, conjunto de entrenamiento, bolsa de palabras 
################################################################################
print("----------------------------------")
print("Cargando archivos...")
tiempo0 = time()
x_setEntrenamientoTweets = [line.rstrip('\n') for line in open('dataTraining.txt')]
y_clases = [line.rstrip('\n') for line in open('clases.txt')]
#bolsaDePalabras = [line.rstrip('\n') for line in open('bolsaDePalabras.txt')]
bolsaDePalabras = [line.rstrip('\n') for line in open('bagOfWords2.txt')]
x_setTesting = [line.rstrip('\n') for line in open('dataTesting.txt')]
#getDistribucionClases('clases.txt')
tiempoFinal = time() - tiempo0
print("Se cargaron datos de clasificación en:" + str(tiempoFinal) + "s")

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
print x_matrizSetEntrenamientoVect;
#transform(raw_documents, copy=True)[source]. 
#Uses the vocabulary and document frequencies (df) learned by fit (or fit_transform).
x_matrizPrueba = vectorizador.transform(x_setTesting)
#matrizVectorizada = np.array(matrizVectorizada, dtype='float_')
tiempoFinal = time() - tiempo0
print("Se ha creado la matriz TF-IDF en {0} s".format(tiempoFinal))
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
scores = cross_val_score(multinomialBY, x_matrizSetEntrenamientoVect, y_clases, cv = 10)
t1 = time() - t0
print np.mean(scores)
print np.std(scores)

multinomialBY.fit(x_matrizSetEntrenamientoVect, y_clases)
print("Temino en {0} s".format(t1))

print("Testing: clasificador bayesiano...")
t0 = time()
res1 = multinomialBY.predict(x_matrizPrueba)
t1 = time() - t0
print("Termino en {0} s".format(t1))
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
t1 = time() - t0
print np.mean(scores)
print np.std(scores)
svm.fit(x_matrizSetEntrenamientoVect, y_clases)
print("Temino en {0} s".format(t1))
print("Probando clasificador SVC...")
t0 = time()
res2 = svm.predict(x_matrizPrueba)
t1 = time() - t0
print("Temino en {0} segundos SVM sin parametros".format(t1))
print("----------------------------------")

print("----------------------------------")
print(" Traning con clasificador SVM : C= 1.0, gamma=0.10000000000000001 ")
t0 = time()
rbf_svc = SVC(kernel='rbf', C= 1.0, gamma=0.10000000000000001)
#clf.fit(matrizVectorizada, tweetsClases)
scores = cross_val_score(rbf_svc, x_matrizSetEntrenamientoVect, y_clases, cv = 10)
t1 = time() - t0
print np.mean(scores)
print np.std(scores)
rbf_svc.fit(x_matrizSetEntrenamientoVect, y_clases)
print("Temino en {0} s".format(t1))
print("Probando clasificador SVC...")
t0 = time()
res3 = rbf_svc.predict(x_matrizPrueba)
t1 = time() - t0
print("Temino en {0} segundos".format(t1))
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
score1=rbf_svc_tunning.score(x_matrizSetEntrenamientoVect, y_clases)
print np.mean(score1)
print np.std(score1)


print("----------------------------------")


################################################################################
# Persistentencia
################################################################################
print("----------------------------------")
print("\n Guardando en disco del entrenamiento...")
time0 = time()
print rbf_svc_tunning.score(x_matrizSetEntrenamientoVect, y_clases)
joblib.dump(vectorizador, 'matVectorizador.dat')
joblib.dump(rbf_svc_tunning, 'clasificadorModelEntrenado.dat')
time1 = time() - time0
print("Finalizo en " + str(time1) + "s")
################################################################################
