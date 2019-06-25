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
    #T_train = feature.feature(Z_train, 10000) #feature extract
    #print(T_train[0])
    #T_test = feature.feature(Z_test, len(Z_test)) #feature extract
    #X_train = np.load("aa.npy")
    #X_test = np .load("bb.npy")
    #np.save("22",X_train)
    #np.save("33",X_test)
    #X_train=np.load('feature_large.npy')
    #X_test=np.load('test_large.npy')
    #X_train = feature.feature(Z_train,60000)
    #X_test=feature.feature(Z_test,10000)
    #np.save("feature_large",X_train)
    #np.save("test_large",X_test)
    X_train = Z_train
    X_test=Z_test
    print(np.dot(X_train[0],X_train[0]))
    print(X_train[0])
    return X_train,y_train,X_test,y_test



