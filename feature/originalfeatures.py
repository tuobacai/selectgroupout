# coding:utf-8
from util.redisinfos import excute

class OriginalFeatures():

    def load(self):
        oids=[]
        oidfile = '/data1/yingjie10/selectgroupout/oidfile.txt'
        files = open(oidfile, 'r')
        for line in files:
            oid=line.strip()
            oids.append(oid)
        return oids

    def extractfea(self,oids):
        redisinfos=excute(oids)
        feafile= '/data1/yingjie10/selectgroupout/feafile.txt'
        files = open(feafile, 'w')
        for oid in redisinfos:
            files.write(oid+';')
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
