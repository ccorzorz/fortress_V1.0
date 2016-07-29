#!/usr/bin/env python
# -*-coding=utf-8-*-
# Auther:ccorz Mail:ccniubi@163.com Blog:http://www.cnblogs.com/ccorz/
# GitHub:https://github.com/ccorzorz
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.fort import *

"""
super bridge,堡垒机入口程序
"""

def help():
    print('''
使用方法:
1. 单台服务器: python3 hostname command
2. 批量操作(逗号隔开服务器): python3 hostname1,hostname2 command
''')

try:
    #将用户传入的参数进行处理,分为命令内容和hostname列表
    cmd = ' '.join(sys.argv[2:])
    host_list = sys.argv[1].split(',')
except:
    help()
else:
    fort(host_list,cmd)

