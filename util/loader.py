# coding:utf-8
'''
加载原始数据
'''
class Loader():
    def __init__(self):
        self.DATA_FILE = '/data1/yingjie10/selectgroupout/data/grouplabel.txt'

    def read(self):
        file = open(self.DATA_FILE, 'r')
        labelres=dict()
        for line in file:
            temp = line.strip().split(',')
            gid = temp[0]
            oid = temp[1]
            label = temp[2]
            labelres[oid] = dict()
            labelres[oid]['gid'] = gid
            labelres[oid]['label'] = label
        return labelres
