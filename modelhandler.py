#coding:utf-8
from numpy import *
from classify.logisticmodel.logisticregression import LogisticRegression
class ModelHandler(object):
    def __init__(self):
        self.oid2info=None
        self.logistic = LogisticRegression()
        self.optimalWeights=None
    '''
    准备data,label
    '''
    def loaddata(self):
        labels=[]
        feas=[]
        for oid in self.oid2info:
            info=self.oid2info[oid]
            label=info['label']
            labels.append(float(label))
            forbidname=['oid','gid','label']
            feaname=[key for key in info.keys() if key not in forbidname]
            fea=[float(info[key]) for key in feaname]
            fea.insert(0, float(1))
            feas.append(fea)
        return mat(feas),mat(labels).transpose()
    '''
    模型训练
    '''
    def train(self):
        train_x, train_y = self.loaddata()
        opts = {'alpha': 0.01, 'maxIter': 20, 'optimizeType': 'smoothStocGradDescent'}
        self.optimalWeights = self.logistic.trainLogRegres(train_x, train_y, opts)

    '''
    模型验证
    '''
    def validate(self):
        test_x, test_y = self.loaddata()
        accuracy = self.logistic.testLogRegres(self.optimalWeights, test_x, test_y)
        print 'The classify accuracy is: %.3f%%' % (accuracy * 100)

    '''
    模型存储
    '''
    def saver(self):
        modelfile = '/data1/yingjie10/selectgroupout/model/lrmodel.txt'
        file = open(modelfile, 'w')
        weights=[]
        optimalWeights=self.optimalWeights.tolist()
        for arr in optimalWeights:
            w=arr[0]
            weights.append(w)
        file.write(str(weights)+'\n')
        file.close()

    def excute(self,oid2info):
        self.oid2info=oid2info
        self.train()
        self.validate()
        self.saver()
        return self.optimalWeights