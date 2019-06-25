import os
import gzip
import  math
import random
import numpy as np
import mnist_reader
import feature
import test
def extract_feature_vector():
    Z_train, y_train = mnist_reader.load_mnist("", 'train') #extract train data
    Z_test, y_test = mnist_reader.load_mnist("", 't10k') #extract test data
    #T_train = feature.feature(Z_train, 10000) #feature extract
    #print(T_train[0])
    #T_test = feature.feature(Z_test, len(Z_test)) #feature extract
    #T_train = np.load("aa.npy")
    #T_test = np .load("bb.npy")
    #np.save("22",X_train)
    #np.save("33",X_test)
    #X_train=np.load('22.npy')
    #X_test=np.load('33.npy')
    X_train = feature.feature(Z_train,60000)
    X_test=feature.feature(Z_test,10000)
    print(len(X_train[0]))
    print(X_train[0])
    return X_train,y_train,X_test,y_test


b = [1 for i in range(10)]
B_max=[1 for i in range(10)]
X_train,y_train,X_test,y_test = extract_feature_vector()
print((X_train[0]))
#np.save('save_featur',X_train)
#np.save('save_test',X_test)
w = [[1 for i in range(len(X_train[0]))] for j in range(10)]
for z in range(50):
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
            w[maxIndex] -= (X_train[i])
            b[maxIndex] -=1
            w[int(y_train[i])] += X_train[i]
            b[int(y_train[i])] +=1
    print(z)
print(test.test_data(w,b,X_test,y_test,10000))
