# coding:utf-8
from util.redisinfos import excute

class OriginalFeatures():

    def load(self):
        oids=[]
        oidfile = '/Users/yingjie10/PycharmProjects/selectgroupout/oidfile.txt'
        files = open(oidfile, 'r')
        for line in files:
            oid=line.strip()
            oids.append(oid)
        return oids

    def extractfea(self,oids):
        redisinfos=excute(oids)
        i=int(0)
        for oid in redisinfos:
            i+=1
            if i<10:
                print 'info:',oid,redisinfos[oid]
        return
if __name__=='__main__':
    fea=OriginalFeatures()
    oids=fea.load()
    fea.extractfea(oids)

    # fea.extractfea(fea.loader.alloids)