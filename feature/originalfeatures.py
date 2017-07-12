# coding:utf-8
from util.redisinfos import excute

class OriginalFeatures():
    def __init__(self):
        self.oids = list()
        self.labelres = dict()

    def load(self):
        oids = []
        oidfile = '/data1/yingjie10/selectgroupout/oidfile.txt'
        files = open(oidfile, 'r')
        for line in files:
            oid = line.strip()
            oids.append(oid)
        self.oids = oids

        labelres = dict()
        labelfile = '/data1/yingjie10/selectgroupout/labelfile.txt'
        file = open(labelfile, 'r')
        for line in file:
            temp = line.strip().split(',')
            gid = temp[0]
            oid = temp[1]
            label = temp[2]
            labelres[oid]=dict()
            labelres[oid]['gid']=gid
            labelres[oid]['label'] = label
        self.labelres = labelres

    def extractfea(self):
        redisinfos=excute(self.oids)
        train= '/data1/yingjie10/selectgroupout/train.txt'
        files = open(train, 'w')
        i=int(0)
        for oid in redisinfos:
            i+=1
            gid=self.labelres[oid]['gid']
            label=self.labelres[oid]['label']
            if i==1:
                files.write('label,oid,gid,'+str(redisinfos[oid].keys()).replace('[','').replace(']','').replace("'",'')+'\n')
            files.write(label+','+oid+','+gid+','+str(redisinfos[oid].values()).replace('[', '').replace(']', '') + '\n')
        files.close()
    def excute(self):
        self.load()
        self.extractfea()
if __name__=='__main__':
    fea=OriginalFeatures()
    fea.extractfea()

    # fea.extractfea(fea.loader.alloids)

