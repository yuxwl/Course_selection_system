#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''

import os
from core import logger
from conf import settings

log_type = "system" #系统日志记录到文件中
system_logger = logger.logger(log_type)


#初始化账户数据
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}


def check_loging(func):
    '''
    检查是否登录
    :param func: 
    :return: 
    '''

    def inner(*args,**kwargs):
        if user_data.get("is_authenticated",None):
            ret = func(*args,**kwargs)
            return ret
        else:
            #登录流程:通过输入用户、密码、取用户对应的ID的账号,再对比密码
            print ("\33[33;1mPlease sign in!\33[0m")
            person = Person()





