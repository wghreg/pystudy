#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

'''                                        
    由于关系数据库的多个表还可以用外键实现一对多、多对多等关联. ORM框架也可以提供两个对象之间的一对多、多对多等功能。
    ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
    正确使用ORM的前提是了解关系数据库的原理。
'''
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    # 一对多
    books = relationship("Book")

class Book(Base):
    __tablename__ = "book"

    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    #
    user_id = Column(String(20), ForeignKey("user.id"))

'''
    pool_size 连接数
    max_overflow 最多多几个连接
    pool_recycle 连接重置周期
    pool_timeout 连接超时时间
'''
s = "mysql+mysqlconnector://root:root@127.0.0.1:3306/boot_test"
engine = create_engine(s, pool_size=10, max_overflow=10)
DBSession = sessionmaker(bind=engine)

session = DBSession()

new_book1 = Book(id='1', name='java', user_id='2')
new_book2 = Book(id='2', name='c++', user_id='2')
new_book3 = Book(id='3', name='python', user_id='2')
session.add(new_book1)
session.add(new_book2)
session.add(new_book3)

session.commit()
session.close()