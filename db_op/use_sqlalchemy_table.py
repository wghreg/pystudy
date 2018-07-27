#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表明称
    __tablename__ = "user"

    #表字段b
    id = Column(String(20), primary_key=True)
    name = Column(String(50))


# 初始化数据库连接
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/boot_test")

# 创建DBSession类型， DBSession对象可视为当前数据库连接
DBSession = sessionmaker(bind=engine)

''' 添加数据 '''
# 创建session对象
session = DBSession()
# 创建新User对象
new_user = User(id='5', name='zhangsan')
# 添加到session
session.add(new_user)
# 提交保存到数据库
session.commit()
# 关闭session
session.close()

''' 查询数据 '''
# 有了ORM，查询出来的可以不再是tuple，而是User对象。
session = DBSession()
# 创建查询，filter是where条件，调用one()返回唯一行，all()返回所有查询的结果集
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性
print("type:", type(User))
print("name:", user.name)
session.close()
''' ORM就是把数据库表的行与相应的对象建立关联，互相转换。'''