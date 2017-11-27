#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''

from conf import settings
from lib.db import Db
import os
import re



class Account(object):
    '''
    账号类
    '''
    db = Db(settings.ACCOUNT_DATABASE) #数据库连接,公共属性
    db_path = db.db_handler()

    def __init__(self,user_name,password,status=settings.STATUS['normal'],
                 authority = settings.AUTHORITY['student'],user_info={}):
        '''
        定义账号属性
        :param user_name: 用户名，字符类型 
        :param password: 密码，字条类型
        :param status: 账号状态和账号账号权限，数字整形
        :param authority: 账号权限，数字整型
        :param user_info: 用户信息，字典类型
        '''
        self.user_name = user_name
        self.password = password
        self.status = status            #0为锁定用户,1为正常
        self.authority = authority      #1为普通学员,2为讲师,8为admin用户
        self.user_info = user_info      #学员、讲师、学校信息

    def show_info(self):
        '''查看user_info属性'''
        print ("account_id: \033\[32;1m{}\033[0m".format(self.account_id))
        if self.user_info:
            for k in self.user_info:
                print  ("{}: \033\[32;1m{}\033[0m".format(k,self.user_info[k]))

    def create(self):
        '''
        创建新账号
        :return: 返回账户实例(自己)
        '''
        #获取自增长ID
        begin_id = 10000
        auth_increment_file = "%s/increment_id" % os.path.dirname(Account.db_path)
        if os.path.exists(auth_increment_file):     #自增长id文件存在时
            line = Account.db.load_pickle_date(auth_increment_file)
            auth_increment_id = int(line) + 1
        else :          #自增长id文件不存在时
            id_list = []        #账户数据文件
            files_list = os.listdir(Account.db_path)
            for f in files_list:
                exist_flag = re.match(r'^(\d{5,})',f)
                if exist_flag: #有账号存在时
                    id_list.append(f)

            if id_list:
                id_list.sort()
                max_id = int(id_list[-1])
                auto_increment_id = max_id +1
            else:
                auto_increment_id = begin_id   #账号数据不存在

        self.account_id = auto_increment_id     #账号ID
        check_flag = self.check_user_name(auto_increment_id)    #检查用户名是否存在
        user_file = "%s/%s" %(Account.db_path,auto_increment_id)
        if not check_flag:  #用户名不存在,才创建用户
            Account.db.dump_pickle_data(auth_increment_file,auth_increment_id)
            Account.db.dump_pickle_data(user_file,self)  #保存账户数据,后面的self暂不是很明白
            return self
        else:
            print ("User name [\033[31;1m%s\033[0m] has been registered!" %self.account_id)
            return self


    def check_user_name(self,account_id):
        '''
        用account_id 检查用户名是否存在于数据库
        :param account_id:  用户名,字符类型
        :return: 存在则为真,否则为假
        '''
        user_names = []     # 初始化用户名数据库
        exist_flag = False  # 初始化存在标记
        user_names_file = "%s/user_names" %Account.db_path
        if os.path.exists(user_names_file):
            user_names = Account.db.load_pickle_date(user_names_file)

            for u_n in user_names:
                if u_n["user_name"] == self.user_name:  #存在
                    exist_flag = u_n["account_id"]
                    return exist_flag

        user_names.append({"account_id":account_id,"user_names":self.user_name})
        result = Account.db.dump_pickle_data(user_names_file,user_names)

        return exist_flag


    def get_account_id(self,user_name):
        '''
        用user_name 查询出account_id
        :param user_name: 
        :return: 
        '''
        exist_flag = False  #初始化存在标记
        user_names_file = "%s/user_names" %Account.db_path
        if os.path.exists(user_names_file):
            user_names = Account.db.load_pickle_date(user_names_file)

            for u_n in user_names:
                if u_n["user_name"] == user_name:   #存在
                    exist_flag = u_n["account_id"]
                    return exist_flag
        return exist_flag

    def get_account_data(self,account_id):
        '''
        获取账号数据
        :param account_id: 账户id
        :return: 
        '''
        exist_flag = False      #初始化存在标记
        user_file = "%s/%s" %(Account.db_path,account_id)
        if os.path.exists(user_file):
            account = Account.db.load_pickle_date(user_file)

            account_data = {
                "account_id":account_id,
                "user_name":self.user_name,
                "password":self.password,
                "status":self.status,
                "authority":self.authority,
                "user_info":self.user_info
            }
            return account
        return exist_flag


    def save_data(self,account_id):
        '''
        保存数据到数据库
        :param account_id: 账户id 
        :return: 
        '''
        user_file = "%s/%s" %(Account.db_path,account_id)
        Account.db.dump_pickle_data(user_file,self)     #保存账号数据
        return True


    def login(self):
        '''
        登录
        因为用户名输入的是用户名，需要转化成account_id来验证
        :return: 
        '''
        account_id = self.get_account_data(self.user_name)
        if account_id:
            account_data = self.get_account_data(account_id)
            user_file = "%s/%s" %(Account.db_path,account_id)
            if os.path.exists(user_file):
                account = Account.db.load_pickle_date(user_file)  #获取用户账号

                if account.password == self.password:       #验证密码
                    if self.status == settings.STATUS['normal']:
                        return account  #返回账号实例
                    else:
                        print ("Account locked,[\033[31;1m %s \033[0m] sign in failed !" % self.user_name)
                else:
                    print ("Password error,[\033[31;1m %s \033[0m] sign in failed !" %self.user_name)
                    return False
            else:
                print ("Account [\033[31;1m %s \033[0m] data exception " %account_id )
        else:
            print ("User name [\033[31;1m %s \033[0m]" % self.user_name)


class Admin(Account):
    '''管理员账号'''

    def mange_teacher(self):
        '''管理学校讲师'''
        pass

    def manager_students(self):
        '''管理学校学员'''
        pass

    def manager_benjis(self):
        '''管理学校班级'''
        pass






