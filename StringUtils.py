#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#

import uuid
import re

def find(reg,str,de=""):
    g = 1
    if isinstance(reg, tuple):
        g = reg[1]
        reg = reg[0]
    m = re.search(reg,str)
    if m:
            return m.group(g)
    return de

def toInt(str,de=None):
    str = find(r"(\d+)",str)
    try:
            return int(str)
    except Exception as err:
            return de

def toFloat(str,de=None):
    str = find(r"(\d+\.?\d*)",str)
    try:
            return float(str)
    except Exception as err:
            return de

def getUuid():
    return str(uuid.uuid1()).replace('-', '')

def if_match_else(str, pars,de=None):
    for par in pars:
        reg = par[0]
        val = par[1]
        m = re.search(reg, str)
        if m:
            return val
    return de

def filter_emoji(desstr,restr=''):
    '''
    过滤表情
    '''
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

def escape_white_space(str):
    if not str:
        return str
    return re.sub(r'\s','',str)
