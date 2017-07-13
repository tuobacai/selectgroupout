# coding:utf-8
class FeatureDiff():
    def __init__(self):
        self.oids2info = dict()
        self.gid2oids = dict()

    def groupmapping(self):
        for oid in self.oids2info:
            info = self.oids2info[oid]
            gid = info['gid']
            if gid not in self.gid2oids:
                self.gid2oids[gid] = dict()
                self.gid2oids[gid][oid] = info
            else:
                self.gid2oids[gid][oid] = info
    '''
    提取组差异特征
    '''
    def handlefea(self):
        name = [' wbfc', 'c', ' i', ' wbcc', ' imn', ' len', ' sscore', ' nfb', ' wrn', ' vpc', ' wcn', ' wbrc']
        for gid in self.gid2oids:
            sumdict=dict()
            for t in name:
                sumdict[t]=float(0)
            for oid in self.gid2oids[gid]:
                info=self.oids2info[oid]
                for key in name:
                    value=float(info[key])
                    sumdict[key]+=value
            for oid in self.gid2oids[gid]:
                info = self.oids2info[oid]
                for key in name:
                    value = float(info[key])
                    valuesum=float(sumdict[key])
                    if value!=0 and valuesum!=0:
                        newvalue=value/valuesum
                        info[key]=newvalue

    def extract_diff(self,oid2info):
        self.oids2info=oid2info
        self.groupmapping()
        self.handlefea()

