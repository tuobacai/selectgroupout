# coding:utf-8
from util.loader import Loader
from util.redisinfos import excute
from feature.featurediff import FeatureDiff

class FeatureHandler():
    def __init__(self):
        self.loader = Loader()
        self.featurediff=FeatureDiff()
        self.oid2info = dict()

    def _extract_original(self):
        labelres= self.loader.read()
        redisinfos = excute(labelres.keys())
        for oid in labelres:
            info=labelres[oid]
            if oid in redisinfos:
                info.update(redisinfos[oid])
        self.oid2info=labelres

    def excute(self):
        self._extract_original()
        self.featurediff.oids2info(self.oid2info)
        i=int(0)
        for oid in self.oid2info:
            i+=1
            if i<3:
                print oid
                print self.oid2info[oid]

    def output(self):
        trainfile = '/data1/yingjie10/selectgroupout/data/trainfea.txt'
        file = open(trainfile, 'w')
        i = int(0)
        for oid in self.oid2info:
            info=self.oid2info[oid]
            i += 1
            label = info['label']
            keyname = [key for key in info.keys() if key != 'label' and key != 'oid' and key != 'gid']
            if i == 1:
                file.write(
                    'label,oid,gid,' + str(keyname).replace('[', '').replace(']', '').replace("'", '') + '\n')
            keyvalue = [info[key] for key in keyname]
            file.write(
                str(label) + ',' + str(oid) + "," + str(gid) + "," + str(keyvalue).replace('[', '').replace(']',
                                                                                                            '').replace(
                    "'", '') + '\n')
        file.close()

if __name__=='__main__':
    handler=FeatureHandler()
    handler.excute()



