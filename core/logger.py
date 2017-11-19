#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''

import logging
from conf import settings

def logger(log_type):
    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # create file handler and set level to waring
    log_file =  '%s/log/%s' %(settings.BASE_DIR,settings)
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    #create formatter
    formatter = logging.Formatter('%(asctims)s - %(name)s - %(levelname)s - %(message)s')

    #add formatter to fh
    fh.setFormatter(formatter)

    #add fh to logger
    logger.addHandler(fh)

    return logger


