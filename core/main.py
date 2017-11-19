#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''

def interactive(menu,menu_dict):
    '''
    与用户交互
    :param menu: 列表提示
    :param menu_dict: 功能列表
    :return: 
    '''
    exit_flag = False
    while exit_flag != "b" :  #不为b，则一直循环
        print (menu)
        user_option = input(">>:").strip()
        if user_option in menu_dict.keys():
            #print (menu_dict[user_option])
            exit_flag = eval(menu_dict[user_option])
        else:
            print ("\033[31;1mOption does not exist!\033[0m")

def logout():
    exit("谢谢使用".center(50,"#"))

def system_student():
    '''
    学员系统
    :return: 
    '''
    menu = '''
----------------- 欢迎进入学员系统 -----------------
    1. \033[33;1m学员注册\033[0m
    2. \033[33;1m进入选课\033[0m
    3. \033[33;1m查看班级\033[0m
    4. \033[33;1m查看个人信息\033[0m
    5. \033[33;1m修改个人信息\033[0m
    6. 后退(注销)
--------------------------------------------------- 
    '''
    memu_dict = {
        '1':''
    }




