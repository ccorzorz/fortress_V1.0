#!/usr/bin/env python
# -*-coding=utf-8-*-
# Auther:ccorz Mail:ccniubi@163.com Blog:http://www.cnblogs.com/ccorz/
# GitHub:https://github.com/ccorzorz

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

"""
数据库初始化核心程序
"""
#生成数据库引擎,并创建一个数据库操作对象
engine = create_engine("mysql+pymysql://cc:123@192.168.4.193:3306/fortress", max_overflow=5)
Base = declarative_base()

#定义users表的类,列为id,user,passwd,ip_id,关联server表中id
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user = Column(String(32))
    passwd = Column(String(32))
    ip_id = Column(Integer, ForeignKey('server.id'))

    __table_args__ = (
        UniqueConstraint('id', name='uix_id_name'),
        Index('ix_id_name', 'user', 'passwd', 'ip_id'),
    )

#定义group表的类,列为id,name,name为唯一索引,并且非空
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

#顶固server表的类
class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(64), unique=True, nullable=False)
    hostname = Column(String(64), nullable=False)
    port = Column(Integer, default=22)

#定义ServerToGroup表,server_id外键server表中的id列,列group_id外键group中的id列
class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))


# 定义初始化数据库函数
def init_db():
    Base.metadata.create_all(engine)


# 顶固删除数据库函数
def drop_db():
    Base.metadata.drop_all(engine)

#实例化数据库操作对象为session
Session = sessionmaker(bind=engine)
session = Session()

# init_db()

# obj = Server(ip='192.168.2.1',hostname='website',port=22)
# session.add(obj)
# session.commit()

# ret=session.query(Group).filter_by(name='asdf').first()
# print(ret.name)

# res = session.query(Group).filter_by(name='asd').all()
# print(res)
# print(bool(res))

# res = session.query(Server).filter_by(ip='192.168.1.1',hostname='web3').all()
# print(res)

# res = session.query(Server.id,Server.ip).all()
# print(res)

# res = session.query(Server).filter(Server.id == 7).all()
# print(res[0].ip,res[0].hostname)

# server_id = session.query(ServerToGroup).filter(ServerToGroup.group_id == 1).all()
# print(server_id[0].server_id)
# users_list=session.query(Users.user,Users.passwd).filter(Users.ip_id==1).all()
# print(users_list)
# res = session.query(Server).filter_by(hostname='webxxx').first()
# print(res)