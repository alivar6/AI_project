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
    #X_train=np.load('feature_large.npy')
    #X_test=np.load('test_large.npy')
    X_train=np.load('feature_law.npy')
    X_test=np.load('test_law.npy')
    #print(np.dot(X_train[0],X_train[0]))
    #print(X_train[0])
    return X_train,y_train,X_test,y_test


b = [1 for i in range(10)]
B_max=[1 for i in range(10)]
X_train,y_train,X_test,y_test = extract_feature_vector()
#np.save('save_featur',X_train)
#np.save('save_test',X_test)
w = [[1 for i in range(len(X_train[0]))] for j in range(10)]
for z in range(27):
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
            tav = min((np.dot(w[maxIndex] ,X_train[i]) - np.dot(w[y_train[i]],X_train[i]) + 1)/(2*(np.dot(X_train[i],X_train[i]))),0.001)
            w[maxIndex] -= (X_train[i])*tav
            b[maxIndex] -=1*tav
            w[int(y_train[i])] += X_train[i]*tav
            b[int(y_train[i])] +=1*tav
    print(z)
print(test.test_data(w,b,X_test,y_test,10000))
