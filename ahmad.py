import os
import gzip
import  math
import numpy as np
import mnist_reader
import feature
import test
Z_train, y_train = mnist_reader.load_mnist("",'train')
Z_test,y_test = mnist_reader.load_mnist("",'t10k')
T_test = feature.feature(Z_test)
X_test = np.zeros((len(Z_test),28*28+113))
for i in range(len(X_test)):
   X_test[i]= np.append(T_test[i],Z_test[i])
print(X_test[0])
b=[1 for i in range(10)]
X_train=np.load('save_pos.npy')
w = [[1 for i in range(len(X_train[0]))] for j in range(10)]
'''''
for i in range(len(T_train)):
    T_train[i]=T_train[i]*10
X_train = np.zeros((len(Z_train),28*28+113))

for i in range(len(X_train)):
   X_train[i]= np.append(T_train[i],Z_train[i])
'''
print(X_train[0])

for z in range(100):
    for i in range(60000):
        maxim, maxIndex = (np.dot(w[5], X_train[i])  + b[5]), 5
        for j in range(len(w)):
            temp = (np.dot(w[j], X_train[i]) +b[j])
            if temp > maxim:
                maxim = temp
                maxIndex = j
        if maxIndex == y_train[i]:
            continue
        else:
            w[maxIndex] -= (X_train[i])*0.001
            b[maxIndex] -=0.001
            w[int(y_train[i])] += X_train[i]*0.001
            b[int(y_train[i])] +=0.001
    print(test.test_data(w, b, X_test, y_test))

print(test.test_data(w,b,X_train,y_train))

#print(test.test_data(w,b))