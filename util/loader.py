# coding:utf-8
import xlrd
import numpy as np
class Loader():
    def __init__(self):
        self.DATA_FILE = '/Users/yingjie10/PycharmProjects/selectgroupout/groupdata.xlsx'
        self.group2oids=dict()
        self.alloids=list()
    # 从.xlsx中读取数据
    def read(self):
        book = xlrd.open_workbook(self.DATA_FILE, encoding_override='utf-8')
        sheet = book.sheet_by_index(0)
        # 得到一个dict,key是gid,value是list,list元素是(oid,标签)
        res =[]
        temp=[]
        for i in range(0, sheet.nrows):
            t = sheet.row_values(i)
            col = t[0]
            cols = t[1]
            if (not col and not cols) :
                res.append(temp)
                temp=[]
            elif i==sheet.nrows-1:
                temp.append(t)
                res.append(temp)
            else:
                temp.append(t)

        for group in res:
            gidstr = str(group[0][0]).split(':')
            gid = gidstr[1]
            grouplist=list()
            for i in range(1,len(group)):
                temp=group[i]
                oid=str(temp[0])
                if oid not in self.alloids:
                    self.alloids.append(oid)
                label=int(temp[1])
                grouplist.append((oid,label))
            self.group2oids[gid]=grouplist
    def output(self):
        labelfile='/Users/yingjie10/PycharmProjects/selectgroupout/labelfile.txt'
        file=open(labelfile,'w')
        oidfile='/Users/yingjie10/PycharmProjects/selectgroupout/oidfile.txt'
        files = open(oidfile, 'w')
        for gid in self.group2oids:
            for ts in self.group2oids[gid]:
                (oid, label)=ts
                file.write(str(gid)+','+str(oid)+','+str(label)+'\n')
        file.close()
        for oid in self.alloids:
            files.write(str(oid)+'\n')
        files.close()




if __name__=='__main__':
    loader=Loader()
    loader.read()
    loader.output()