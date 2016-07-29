#!/usr/bin/env python
# -*-coding=utf-8-*-
# Auther:ccorz Mail:ccniubi@163.com Blog:http://www.cnblogs.com/ccorz/
# GitHub:https://github.com/ccorzorz

import paramiko

"""
使用paramiko 远程执行命令
"""

class Cmd:
    def __init__(self, ip, port, username, passwd, hostname):
        """
        构造方法,初始化ssh
        :param ip: IP地址
        :param port: 端口
        :param username:用户名
        :param passwd: 密码
        :param hostname: 服务器的hostname
        :return:
        """
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, port, username, passwd)
        self.hostname = hostname
        self.stdin = None
        self.stdout = None
        self.stderr = None

    def run(self, command):
        """
        执行命令函数
        :param command: 用户输入的命令
        :return:
        """
        self.stdin, self.stdout, self.stderr = self.ssh.exec_command(command)
        self.stdout = self.stdout.read().decode('utf8')
        self.stderr = self.stderr.read().decode('utf8')
        #如果出错,输出结果为错误信息,否则为命令操作结果
        if self.stderr:
            out = self.stderr
        else:
            out = self.stdout
        self.ssh.close()
        #便于用户区分是哪台服务器的输出结构
        print('%s\n==============\n%s\n=============='%(self.hostname,out))


