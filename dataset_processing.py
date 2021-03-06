# -*- coding: utf-8 -*-
"""Dataset_Processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YpP6c3MHTyxQTanD2i6WS8HsuQfzKDmG

**Loading your dataset from uploaded csv file**
"""

from google.colab import drive
drive.mount('/content/drive')

from numpy import genfromtxt
path = '/content/drive/MyDrive/data/iris.csv'
dataset = genfromtxt(path, delimiter = ',')
#print(dataset)

import random
list_data = dataset.tolist()
random.shuffle(list_data)
#print(list_data)

from random import random
Train_set=[]
Val_set=[]
Test_set=[]
for S in list_data:
  R=random()
if R >= 0 and R <= 0.7:
  Train_set.append(S)
elif R > 0.7 and R <= 0.85:
  Val_set.append(S)
else:
    Test_set.append(S)

from scipy.spatial import distance
import operator
k = 15
correct = 0
for V in Val_set:
  majority_class  = {}
  L = {}
for T in Train_set:
  xy = distance.euclidean(V[0:(len(V)-1)], T[0:(len(T)-1)])
  L[ed] = T
  sorted_L = sorted(L.keys())
  #print(sorted_L)
  #print(len(sorted_L))
  count = 1
for x in sorted_L:
  result = int(L[x][-1])
  #print(L[x])
if result in majority_class.keys():
  majority_class[int(L[x][-1])] = majority_class[int(L[x][-1])]+1
else:
  majority_class[int(L[x][-1])] = 1
  count = count + 1
if(count > k):
  break
  value = max(majority_class.items(), key=operator.itemgetter(1))[0]
if(int(V[-1]) == value):
  correct = correct + 1
accuracy = (correct/len(Val_set))*100
print(accuracy)

from scipy.spatial import distance
import operator
k = 15
correct = 0
for V in Test_set:
  majority_class = {}
  L = {}
for T in Train_set:
  xy = distance.euclidean(V[0:(len(V)-1)], T[0:(len(T)-1)])
  L[ed] = T
  sorted_L = sorted(L.keys())
#print(len(sorted_L))
count = 1
for x in sorted_L:
  result = int(L[x][-1])
  #print(L[x])
if result in majority_class.keys():
  majority_class[int(L[x][-1])] = majority_class[int(L[x][-1])]+1
else:
  majority_class[int(L[x][-1])] = 1
  count = count + 1
  if(count > k):
    break
    value = max(majority_class.items(), key=operator.itemgetter(1))[0]
if (int(V[-1]) == value):
  correct = correct + 1
  #print(correct)
accuracy = (correct/len(Test_set))*100
print(accuracy)