#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define functions relative to bcv.
"""

import gnttb.sblgnt

def bcv2str(bcv):
    """Convert a bcv into a string using the BJ convention.
    """

    return '{} {}, {}'.format(gnttb.sblgnt.sblgnt_books[bcv[0:2]][1], int(bcv[2:4]), int(bcv[4:6]))
