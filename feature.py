import numpy as np
import math
def feature(X_train):
    f=np.zeros((len(X_train),56+56+1))
    for i in range(len(X_train)):
        for j in range(28):
            count = 0
            for z in range(len(X_train[0])):
                if((z//28) == j and X_train[i][z] > 60):
                    count+=1
            f[i][j] = count
            med = 0;
            for z in range(len(X_train[0])):
                if ((z // 28) == j and X_train[i][z] > 60):
                    med+=1
                if(med > (count/2)):
                    f[i][j+28] = z%28
                    break
            count = 0
            for z in range(len(X_train[0])):
                if ((z % 28) == j and X_train[i][z] > 60):
                    count += 1
            f[i][j+56] = count
            med = 0;
            for z in range(len(X_train[0])):
                if ((z % 28) == j and X_train[i][z] > 60):
                    med += 1
                if (med > (count / 2)):
                    f[i][j + 56+28 ] = z // 28
                    break
        count = 0;
        for j in range(len(X_train[0])):
            if(j%28 <14 and X_train[i][j] > 60):
                count +=1
            if (j % 28 >= 14 and X_train[i][j] > 60):
                count -=1
        if(count < 0):
            count*=-1
        if(count == 0):
            count =0.01
        f[i][56+56]=count

    return f*10


