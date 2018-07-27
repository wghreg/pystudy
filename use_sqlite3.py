#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
SQLite是一种嵌入式数据库，它的数据库就是一个文件。
由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
'''
import sqlite3

'''
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；

连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。

由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。
'''
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