#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_LEVEL = logging.INFO

ACCOUNT_DATABASE = {
    'engine':'file_storage',
    'name':'account',
    'path':'%s/db' %BASE_DIR
}

BASE_DATABASE = {
    'engine':'file_storage',
    'name':'base',
    'path':'%s/db' %BASE_DIR
}

LOG_TYPES = {
    'system':'system.log'
}

AUTHORITY = {
    'student':1,
    'teacher':2,
    'admin':8
}

STATUS = {
    'normal':1,
    'locked':2
}