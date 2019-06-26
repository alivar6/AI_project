import numpy as np
import math
import mnist_reader
def feature(X_train,lenth):
    f=np.zeros((lenth,56+56+56))
    for i in range(lenth):
        for j in range(28):
            count = 0
            for k in range(28):
                if(( X_train[i][j*28 +k] > 40)):
                    count+=1

            f[i][j] = count*20
            med = 0
            for k in range(28):
                if ((X_train[i][j * 28 + k] > 40)):
                    med+=1
                if(med > (count/2)):
                    f[i][j+28] = k*20
                    break;

            count = 0

            for k in range(28):
                if ( X_train[i][j+28* k] > 40):
                    count += 1

            f[i][j+56] = count*20
            med = 0;

            for k in range(28):
                if ( X_train[i][j+28* k] > 40):
                    med += 1
                if (med > (count / 2)):
                    f[i][j + 56+28 ] = k*20
                    break

            med = 0

            for k in range(28):
                if ( k<27 and X_train[i][28*k+j] <40 and X_train[i][28*k+28+j] > 40):
                    med += 1
                if (k < 27 and X_train[i][28 * k + j] > 40 and X_train[i][28 * k + 28 + j] < 40):
                    med += 1
            f[i][j + 112] = med*200
            med = 0
            for k in range(28):
                if ( k<27 and  X_train[i][j*28 + k]< 40 and X_train[i][j*28 + k+1 ] > 40):
                    med += 1
                if (k < 27 and X_train[i][j * 28 + k] > 40 and X_train[i][j * 28 + k + 1] < 40):
                    med += 1
            f[i][j + 112 + 28] = med * 200
    x1 = np.zeros((lenth, 28 * 28 + 56 * 3))
    for i in range(lenth):
        x1[i] = (np.append(f[i],X_train[i]))
    return x1


def extract_feature_vector():
    Z_train, y_train = mnist_reader.load_mnist("", 'train') #extract train data
    Z_test, y_test = mnist_reader.load_mnist("", 't10k') #extract test data
    X_train=np.load('feature_law.npy')
    X_test=np.load('test_law.npy')
    return X_train,y_train,X_test,y_test


def extract_feature_low(Z_train):
    X_train = np.zeros((len(Z_train),len(Z_train[0])))
    for i in range(len(X_train)):
        for j in range(len(X_train[0])):
            X_train[i][j] = Z_train[i][j]/200;
    return X_train




