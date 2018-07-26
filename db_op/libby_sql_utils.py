#! /usr/bin/env python3
# *-* coding:utf-8 *-*

''' 支持增删改查功能的连接池模块'''
from libby_db_pools import getConn, reConn
import traceback

 """
    测试连接池连接是否正常
    return：
    res：True：正常，False：不正常
    msg：如果不正常，为异常信息
"""
def test_conn():
    test_sql = '''
        select 1
    '''
    conn = None
    cur = None
    res = False
    msg = ""
    try:
        conn = getConn()
        cur = conn.cursor()
        cur.execute(test_sql)
        res = cur.fetchall()
        res = True
    except Exception as e:
        traceback.print_exc()
        msg = e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        return res, msg

''' 重新创建连接 '''
def call_reConn():
    reConn()


 """
    dbutils 数据连接池
        只能执行数据查询sql语句,否则会抛错
    @parm: 要执行的sql语句
    @return:
        []:查询结果为空
        None:sql语句执行失败,出现异常
                二维list:正常结果
"""
def p_query(sql):
    conn = None
    cur = None
    res = None
    try:
        conn = getConn()
        cur = conn.cursor()
        cur.execute(test_sql)
        res = cur.fetchall()
    except Exception as e:
        call_reConn()
        traceback.print_exc()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        return res