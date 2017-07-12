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
        feafile= '/Users/yingjie10/PycharmProjects/selectgroupout/feafile.txt'
        files = open(feafile, 'w')
        for oid in redisinfos:
            files.write(oid+'\n')
            files.write(str(redisinfos[oid])+'\n')
        files.close()
    def excute(self):
        oids = self.load()
        self.extractfea(oids)
if __name__=='__main__':
    fea=OriginalFeatures()
    oids=fea.load()
    fea.extractfea(oids)

    # fea.extractfea(fea.loader.alloids)