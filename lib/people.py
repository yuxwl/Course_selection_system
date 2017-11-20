#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''

class Person(object):
    '''人基类'''
    def __init__(self,name=None,age=None,sex=None,account = None):
        '''
        定义人的基本属性
        :param name: 名字,字符类型
        :param age: 年龄,数字类型
        :param sex: 性别,字符类型
        :param account: 账号,实例
        '''
        self.name = name
        self.age = age
        self.sex = sex
        self.account = account

    def show_info(self):
        '''查看account的user_info属性'''
        print (" User info ".center(50,"-"))
        print (" account id:",self.account.account_id)
        if self.account.user_info:
            print(self.account.user_info)

        print ("-".center(50,'-'))

    def enroll(self,authority =1):
        '''
        注册账号
        :param authority: 
        :return: 返回账号实例
        '''
        user_Name = input("Please input user name >>: ").strip()
        password = input("Please input password >>: ").strip()
        re_password = input("Please input password confirmation >>: ").strip()
        if password != re_password:
            print("\33[31;1mPassword do not match!\33[0m")
            return False
        status = 1
        account = Account()