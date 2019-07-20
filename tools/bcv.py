#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define functions relative to bcv.
"""

import gnttb.sblgnt
import gnttb.bcv

def bcv2str(bcv):
    """Convert a bcv into a string using the BJ convention.
    """

    if len(bcv) == 6:
        return '{} {}, {}'.format(gnttb.sblgnt.sblgnt_books[bcv[0:2]][1], int(bcv[2:4]), int(bcv[4:6]))
    else:
        bcv_start, bcv_end = gnttb.bcv.splitBcv(bcv)

        if bcv_start[2:4] == bcv_end[2:4]:
            # same chapter
            return '{} {}, {}-{}'.format(gnttb.sblgnt.sblgnt_books[bcv_start[0:2]][1], int(bcv_start[2:4]),
                    int(bcv_start[4:6]), int(bcv_end[4:6]))

        else:
            # different chapter
            return '{} {}, {} − {}, {}'.format(gnttb.sblgnt.sblgnt_books[bcv_start[0:2]][1],
                    int(bcv_start[2:4]), int(bcv_start[4:6]), 
                    int(bcv_end[2:4]) ,int(bcv_end[4:6]))
