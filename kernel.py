import numpy as np
import math
import time
import feature

def RBF_Kernel(x , y , gamma):
    dist = np.linalg.norm(x-y)
    power = -1 * gamma * pow(dist , 2)
    return np.exp(power)

trainLength = 500
testlenght =500
a = time.time()
alphas = [[0 for i in range(trainLength)] for j in range(10)]
kernels = [[0 for i in range(trainLength)] for j in range(trainLength)]
data,labels,testData,testlabels = feature.extract_feature_vector()
kernels_test = [[0 for i in range(trainLength)] for j in range(testlenght)]

for i  in range(trainLength):
    for j in range(trainLength):
        kernels[i][j] = RBF_Kernel(data[i],data[j],0.000001)


for i  in range(testlenght):
    for j in range(trainLength):
        kernels_test[i][j] = RBF_Kernel(testData[i],data[j],0.000001)
print(kernels[0][100])


maxIndex = 0
count = 0
for z in range(5):
    count = 0
    for i in range(trainLength):



        maxim = - (10**30)
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
    print(count/10)



correct = 0

for i in range(testlenght): #classify test datas

    maxim = - (10 ** 30)
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

