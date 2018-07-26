#! /usr/bin/env python3
# *-* coding:utf-8 *-*

# python3 已经不支持mysql-python, 使用pymysql代替( https://github.com/PyMySQL/PyMySQL )
# pip install PyMySQL
# pip install dbutils


from DBUtils.PooledDB import PooledDB
import mysql

conn_args = {
    'host': '127.0.0.1',
    'port': 3306,
    'charset': 'utf-8',
    'database': 'boot_test',
    'user': 'root',
    'password': 'root'
}
'''
    mincached 启动时开启的闲置连接数。默认为0，即开始时不创建连接
    maxcached 连接池中允许闲置的最多连接数。默认为0，不闲置连接
    maxshared 允许共享的最大连接数。默认为0，即所有连接都是专用的。如果达到最大数量，被请求为共享的连接会被共享使用
    maxconnections 创建连接池的最大数量。默认为0，表示不限制
    blocking 连接池达到最大数量时是否阻塞连接。默认为0或False，代表返回错误<toMany....>; 其他表示阻塞直到连接数减少，连接被分配
    maxusage 允许单个连接的最大复用次数。默认为0或False，表示不限制。当达到最大数时，连接会自动重新连接(关闭和重新打开)
    setsession 每个session会话 可选的sql命令列表 eg.['set datestyle tog german', .....]
'''
args = {10, 10, 30, 100, True, 0, None}

class DbManager():
    def __init__(self, *args, **kwargs):
        try:
            self._pool = PooledDB(mysql, **args, **conn_args)
        except Exception, e:
            print("The parameters for DBUtils is :", conn_args)
    
    def _getConn(self):
        return self._pool.connection()

_dbManager = DbManager()

''' 获取数据库连接 '''
def getConn():
    return _dbManager._getConn()


def _reConn():
    global _dbManager
    re = False
    try:
        _dbManager = DbManager()
        re = True
    except:
        import traceback
        traceback.print_exc()
    finally:
        return re



import datetime

def reConn():
    print("%s: now try to reconnect Database!" % (datetime.datetime.now()))
    flag = _reConn()
    if flag:
        print("%s reconnect database success!" % (datetime.datetime.now()))
    else:
        print("%s reconnect database failed!" % (datetime.datetime.now()))


pool = PooledDB(mysql,)


