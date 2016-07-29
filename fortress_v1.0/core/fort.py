#!/usr/bin/env python
# -*-coding=utf-8-*-
# Auther:ccorz Mail:ccniubi@163.com Blog:http://www.cnblogs.com/ccorz/
# GitHub:https://github.com/ccorzorz

import sys, os, threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.host_handle import *
from core.cmd_op import *

"""
多线程执行用户命令
"""
def fort(host_list,cmd):
    #将出入的hostname列表进行处理,
    info_list = []
    for item in host_list:
        info_list.append(find_info(item))
    for item in info_list:
        #如果为字符串,说明为数据中无此hostname
        if type(item) == str:
            print(item)
        else:
            #否则,将列表中的信息赋予变量
            ip, port, username, passwd, hostname = item
            #实例化对象
            obj = Cmd(ip, port, username, passwd, hostname)
            #多线程执行
            t =  threading.Thread(target=obj.run, args=(cmd,))
            t.start()