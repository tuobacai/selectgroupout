#coding=utf-8
from featurehandler import FeatureHandler
from modelhandler import ModelHandler
class Main(object):
    def __init__(self):
        self.feahandelr=FeatureHandler()
        self.modelhandler=ModelHandler()
        self.oid2info=dict()
    def excute(self):
        self.oid2info=self.feahandelr.excute()
        self.weights=self.modelhandler.excute(self.oid2info)


