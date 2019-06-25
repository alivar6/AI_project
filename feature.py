import numpy as np
import math
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


