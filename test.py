import numpy as np
import mnist_reader
import feature

def test_data(w,b,X_test,y_test):
    correct = 0
    for i in range(1000):  # classify test datas
        maxim, maxIndex =( np.dot(w[0], X_test[i])+b[0]), 0
        for j in range(len(w)):
            temp = np.dot(w[j], X_test[i]) + b[j]
            if temp > maxim:
                maxim = temp
                maxIndex = j
        if maxIndex == y_test[i]:
            correct += 1
    return (correct * 100 / 1000)