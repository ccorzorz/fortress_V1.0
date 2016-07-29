#!/usr/bin/env python
# -*-coding=utf-8-*-
# Auther:ccorz Mail:ccniubi@163.com Blog:http://www.cnblogs.com/ccorz/
# GitHub:https://github.com/ccorzorz

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import core.manager
"""
管理后台入口
"""

if __name__ == '__main__':
    core.manager.main()