#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: logconf.py
# $Date: Fri Jan 02 01:22:55 2015 +0800
# $Author: jiakai <jia.kai66@gmail.com>

import logging
import os

log_fout = None
def write_file(val):
    pass

def init():
    global log_fout
    global write_file
    if os.getenv('NEUPACK_LOG_FILE'):
        log_fout = open(os.getenv('NEUPACK_LOG_FILE'), 'a')
        def write_file(val):
            while True:
                s = val.find('\x1b')
                if s == -1:
                    break
                t = val.find('m', s)
                assert t != -1
                val = val[:s] + val[t+1:]
            log_fout.write(val)
            log_fout.write('\n')
            log_fout.flush()

class _LogFormatter(logging.Formatter):
    def format(self, record):
        date = '\x1b[32m[%(asctime)s %(lineno)d@%(filename)s:%(name)s]\x1b[0m'
        msg = '%(message)s'
        if record.levelno == logging.WARNING or record.levelno == logging.CRITICAL:
            fmt = '{} \x1b[1;31mWRN\x1b[0m {}'.format(date, msg)
        elif record.levelno == logging.ERROR:
            fmt = '{} \x1b[1;4;31mERR\x1b[0m {}'.format(date, msg)
        else:
            fmt = date + ' ' + msg
        self._fmt = fmt

        val = super(_LogFormatter, self).format(record)
        write_file(val)
        return val

old_getlogger = logging.getLogger
def new_getlogger(name=None):
    logger = old_getlogger(name)
    if getattr(logger, '_init_done__', None):
        return logger
    logger._init_done__ = True
    logger.propagate = False
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(_LogFormatter(datefmt='%d %H:%M:%S'))
    handler.setLevel(logging.INFO)
    del logger.handlers[:]
    logger.addHandler(handler)
    return logger

logging.getLogger = new_getlogger
init()
