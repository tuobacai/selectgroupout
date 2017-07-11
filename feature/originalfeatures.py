# coding:utf-8
from util.redisinfos import excute
from util.loader import Loader
class OriginalFeatures():
    def __init__(self):
        self.loader=Loader()
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
    fea.loader.read()
    fea.extractfea(fea.loader.alloids)