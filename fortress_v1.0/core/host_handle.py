#!/usr/bin/env python
# -*-coding=utf-8-*-
# Auther:ccorz Mail:ccniubi@163.com Blog:http://www.cnblogs.com/ccorz/
# GitHub:https://github.com/ccorzorz

import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.init_db import *

def find_info(hostname):
    """
    通过用户传入的hostname,从数据库中查询服务器的相关信息,并生成列表
    :param hostname: hostname
    :return: 生成的结果
    """
    #如果查询的hostname有相关信息,取得相关值
    if session.query(Server).filter_by(hostname=hostname).first():
        res = session.query(Server).filter_by(hostname=hostname).first()
        sip = res.ip
        port = res.port
        sid = res.id
        res_server = session.query(Users.user,Users.passwd).filter(
            Users.ip_id == sid).first()
        username = res_server.user
        passwd = res_server.passwd
        #生成列表
        host_info = [sip,port,username,passwd,hostname]
    else:
        #否则,定义为未知的hostname
        host_info = 'Unknow hostname:%s'%hostname

    return host_info