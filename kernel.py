import numpy as np
import math
import time
import feature

def RBF_Kernel(x , y , gamma):
    dist = np.linalg.norm(x-y)
    power = -1 * gamma * pow(dist , 2)
    return np.exp(power)

trainLength = 10000
testlenght =5000
a = time.time()
alphas = [[0 for i in range(trainLength)] for j in range(10)]
kernels = [[0 for i in range(trainLength)] for j in range(trainLength)]
data,labels,testData,testlabels = feature.extract_feature_vector()
kernels_test = [[0 for i in range(trainLength)] for j in range(testlenght)]
''''
for i  in range(trainLength):
    for j in range(trainLength):
        kernels[i][j] = RBF_Kernel(data[i],data[j],0.008)
    if (i % 500 == 0):
        print("train :")
        print(i)


for i  in range(testlenght):
    for j in range(trainLength):
        kernels_test[i][j] = RBF_Kernel(testData[i],data[j],0.008)
    if (i % 500 == 0):
        print("test :")
        print(i)
'''
#print(kernels[0][100])
#np.save("train_kernel",kernels)
#np.save("test_kernel",kernels_test)
kernels = np.load("train_kernel.npy")
kernels_test = np.load("test_kernel.npy")
print("asd")
maxIndex = 0
count = 0
for z in range(10):
    count = 0
    for i in range(trainLength):



        maxim = - (10**7)
        current = 0
        for k in range(10):

            current = 0

            for j in range(trainLength):
                #current += alphas[k][j] * math.exp(-1 * np.dot((data[i] - data[j]), (data[i] - data[j])))
                #current += np.dot(data[i], np.multiply(alphas[k][j], data[j]))
                current += alphas[k][j] * kernels[i][j]
            if current > maxim:
                maxim = current
                maxIndex = k

        if labels[i] == maxIndex:
            count = count+1
            continue
        else:
            alphas[maxIndex][i] -= 1
            alphas[int(labels[i])][i] += 1
    print(z)
    print(count/trainLength * 100)



correct = 0

for i in range(testlenght): #classify test datas

    maxim = - (10 ** 7)
    maxIndex = 0
    for k in range(10):
        current = 0
        for j in range(trainLength):
            current += alphas[k][j] * kernels_test[i][j]
        if current > maxim:
            maxim = current
            maxIndex = k
    if testlabels[i] == maxIndex:
        correct += 1
print(time.time() - a)
print(correct * 100/testlenght)

