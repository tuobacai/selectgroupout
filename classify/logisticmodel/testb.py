# coding:utf-8

from numpy import *
import matplotlib.pyplot as plt
import time
from logisticregression import LogisticRegression


def loadData():
    train_x = []
    train_y = []
    fileIn = open('/Users/yingjie10/PycharmProjects/selectgroupout/data/traindata.txt')
    cnt=int(0)
    feaname=[]
    for line in fileIn.readlines():
        lineArr = line.strip().split(',')
        cnt+=1
        if cnt==1:
            feaname=lineArr
        else:

            fea=[float(i) for i in lineArr[2:]]
            fea.insert(0,float(1))
            # train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
            train_x.append(fea)
            train_y.append(float(lineArr[0]))
    return mat(train_x), mat(train_y).transpose()


logistic = LogisticRegression()
## step 1: load data
print "step 1: load data..."
train_x, train_y = loadData()
# print train_x
# print train_y
test_x = train_x
test_y = train_y

## step 2: training...
print "step 2: training..."
opts = {'alpha': 0.00001, 'maxIter': 2000, 'optimizeType': 'smoothStocGradDescent'}
optimalWeights = logistic.trainLogRegres(train_x, train_y, opts)
print 'optimalWeights:',optimalWeights

## step 3: testing
print "step 3: testing..."
accuracy = logistic.testLogRegres(optimalWeights, test_x, test_y)

## step 4: show the result
print "step 4: show the result..."
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
# logistic.showLogRegres(optimalWeights, train_x, train_y)
