#!/usr/bin/env python
# -*-coding=utf-8-*-
# Auther:ccorz Mail:ccniubi@163.com Blog:http://www.cnblogs.com/ccorz/
# GitHub:https://github.com/ccorzorz

import os, sys, prettytable

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.init_db import *
import core.pwd_handle


def add_group():
    """
    添加服务器组函数,操作数据库表为Group表
    :return:
    """
    inp = input('请输入服务组名称:')
    #如果已存在组名,提示,否则写入数据库中
    if session.query(Group).filter_by(name=inp).all():
        print('%s组已存在!' % inp)
    else:
        obj = Group(name=inp)
        session.add(obj)
        session.commit()
        print('%s组添加成功!' % inp)


def add_server():
    """
    添加服务器信息,操作表对象为Server,服务器IP为唯一
    :return:
    """
    #如果IP存在,提示用户
    IP = input('请输入服务器IP地址:')
    if session.query(Server).filter_by(ip=IP).all():
        print('此IP信息数据库中已存在!')
    else:
        #否则数据端口号,并且判断端口号是否为数字
        host_name = input('请输入hostname:')
        if session.query(Server).filter_by(hostname=host_name).all():
            print('此hostname已存在!')
        else:
            PORT = input('管理端口:')
            try:
                PORT = int(PORT)
            except:
                print('端口设置错误!')
            else:
                #如果正确,将相关服务器信息写入数据库中
                obj = Server(ip=IP, hostname=host_name, port=PORT)
                session.add(obj)
                session.commit()
                print('添加成功')
                link_group(IP)


def add_user():
    """
    定义添加管理员帐号函数
    :return:
    """
    #打印已有服务器信息,
    res = session.query(Server.id, Server.ip).all()
    num_list = []
    for item in res:
        num, ip = item
        num_list.append(num)
        print(num, ip)
    num = input('请选择对应的IP地址序列号:')
    #选择服务器相信ID,进行关联
    try:
        num = int(num)
    except:
        print('选择有误!')
    else:
        if num in num_list:
            user_name = input('输入管理员用户名:')
            if session.query(Users).filter_by(ip_id=num, user=user_name).all():
                print('数据库中存在此IP地址的%s用户' % user_name)
            else:
                passwd = input('请输入管理用户的密码:')
                # passwd = core.pwd_handle.md5_pwd(passwd)
                #相关信息写入数据库中
                obj = Users(user=user_name, passwd=passwd, ip_id=num)
                session.add(obj)
                session.commit()
        else:
            print('选择有误!')


def link_group(IP):
    """
    关联服务器组函数,选择相关服务器组,对服务器进行关联,操作对象为server表和ServerToGroup表
    :param IP:
    :return:
    """
    while True:
        res_group = session.query(Group.id, Group.name).all()
        for item in res_group:
            gid, name = item
            print(gid, name)
        gid = input('请输入要关联服务器组的序列号:')
        try:
            gid = int(gid)
        except:
            print('选择有误!')
        else:
            if 0 < gid <= len(res_group):
                server_id = session.query(Server).filter_by(ip=IP).all()[0].id
                obj = ServerToGroup(server_id=server_id, group_id=gid)
                session.add(obj)
                session.commit()
                print('关联成功')
                break
            else:
                print('选择有误!')


def exit_manager():
    """
    退出函数
    :return:
    """
    exit('系统退出!')

#函数名列表
menu_list = [add_group, add_server, add_user, exit_manager ]

def show_menu():
    """
    打印主菜单函数
    :return:
    """
    row = prettytable.PrettyTable()
    row.field_names=['添加服务器组','添加服务器信息','添加管理帐号','退出系统']
    row.add_row([0,1,2,'3&q'])
    print(row)

def main():
    """
    主函数,登录成功后打印主菜单,选择对应操作并执行
    :return:
    """
    admin_user = input('请输入管理帐号:')
    admin_pwd = input('请输入管理员密码:')
    if admin_user == 'admin' and admin_pwd == 'admin':
        while True:
            show_menu()
            inp = input('请选择响应对应功能序列号:')
            if inp == 'q':
                exit_manager()
            try:
                inp = int(inp)
            except:
                print('选择有误!!')
            else:
                if inp < len(menu_list):
                    menu_list[inp]()
                else:
                    print('选择有误!!')

