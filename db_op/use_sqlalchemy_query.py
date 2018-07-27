#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# date: 2018/7/26 0026 下午 18:54

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    books = relationship("Book")

class Book(Base):
    __tablename__ = "book"
    
    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    user_id = Column(String(20), ForeignKey("user.id"))

conn_str = "mysql+mysqlconnector://root:root@localhost:3306/boot_test"
engine = create_engine(conn_str, pool_size=10, max_overflow=10)

DBSession = sessionmaker(engine)
session = DBSession()

users = session.query(User).filter(User.id=='2').all()

for u in users:
    books = u.books
    print(u)
    print(books)
    print("-"*20)
    print(u.name)
    for b in books:
        print(" "*4, "-"*2, b.name)
    
    print("-"*20)

session.close()