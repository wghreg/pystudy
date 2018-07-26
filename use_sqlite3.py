#! /usr/bin/env python3
# *-* coding:utf-8 *-*

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key, name varchar(50))')
# cursor.execute('insert into user(id, name) values("1", "ZhangSan")')
# conn.commit()

# cursor.execute('insert into user(id, name) values("2", "LiSi")')
# conn.commit()

users = cursor.execute('select * from user')
for u in users:
    print(u)

# 关闭连接
cursor.close()
conn.close()