#! /usr/bin/env python3
# *-* coding:utf-8 *-*

# pip install mysql-connector-python
# 或
# pip install mysql-connector


import mysql.connector

# 获取连接
# conn = mysql.connector.connect(user='root', password='root@123', host='192.168.1.68', database='ocr_recognition')
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='boot_test')
cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key, name varchar(50))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'ZhangSan'])
# 提交并关闭游标
conn.commit()
cursor.close()

# 重新获取连接
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)

# 关闭连接
cursor.close()
conn.close()