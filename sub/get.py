#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the get sub-command.
"""

import gnttb.get

from tools import bcv

def get(args):
    """Get a verse given its bcv.
    """

    verse = gnttb.get.get(args.bcv)
    print('{} : {}'.format(bcv.bcv2str(verse.bcv), verse))
