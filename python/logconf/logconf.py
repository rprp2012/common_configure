# -*- coding: utf-8 -*-
# Date: April 9, 2016

import logging
import os

log_fout = None
def write_file(val):
    pass

class _LogFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%'):
        super(_LogFormatter, self).__init__(fmt, datefmt, style)

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
        # if in python3, then modify self._style._fmt 
        try:
            self._style._fmt = fmt
        except Exception:
            pass

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
