#coding:utf-8
import redis

def _once_get_redis_infos(oids, prefix, fields, conn):
    pipe = conn.pipeline(transaction=False)
    for oid in oids:
        rkey = prefix + str(oid)
        pipe.hmget(rkey, fields)
    ret = pipe.execute()
    return ret

'''
   读取文章在redis中的信息
   prefix:  C: / S: / V:
'''
def get_oids_redisinfo(oids, prefix, fields2default):
    ret = {}
    rlocal = "/var/run/nutcracker_article_r.sock"
    conn = redis.Redis(unix_socket_path=rlocal)
    rest = len(oids)
    length = 500
    begin = 0
    fields = fields2default.keys()
    while rest > 0:
        l = min(length, rest)
        part_oids = oids[begin:begin + l]
        infolist = _once_get_redis_infos(part_oids, prefix, fields, conn)
        for idx, oid in enumerate(part_oids):
            if infolist[idx]:
                info = zip(fields, infolist[idx])
                infodict = {}
                for field, val in info:
                    if not val:
                        infodict[field] = fields2default[field][1]
                    else:
                        type = fields2default[field][0]
                        if type == "int":
                            val = int(float(val))
                        elif type == "str":
                            val = str(val)
                        infodict[field] = val
                ret[oid] = dict(infodict)
        rest -= l
        begin += l
    return ret

def excute(oids):
    REDIS_FIELDS = {
        "imn": ("int", 0),
        "im": ("int", 0),
        "wrn": ("int", 0),
        "vpc": ("int", 0),
        "wcn": ("int", 0),
        "nfb": ("int", 0),
        "wbrc": ("int", 0),
        "wbcc": ("int", 0),
        "wbfc": ("int", 0),
        "sscore": ("int", 50),  # source打分
        "svtype": ("int", -1),  # 普通用户
        "len": ("int", 0),  # 文章长度
    }
    S_REDIS_FIELDS = {
        "i": ("int", 0),
        "c": ("int", 0),
    }
    redisinfos =get_oids_redisinfo(oids, "C:", REDIS_FIELDS)
    sredisinfos =get_oids_redisinfo(oids, "S:", S_REDIS_FIELDS)
    print 'redis:',len(redisinfos),len(sredisinfos)
    # 合并redis数据
    for oid, redisinfo in redisinfos.iteritems():
        if oid in sredisinfos:
            redisinfo.update(sredisinfos[oid])
    return redisinfos
