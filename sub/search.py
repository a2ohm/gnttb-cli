#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the search sub-command.
"""

import gnttb.search
import gnttb.sblgnt

from tools import bcv

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# def bcv2str(bcv):
#     """Convert a bcv into a string using the BJ convention.
#     """
# 
#     return '{} {}, {}'.format(gnttb.sblgnt.sblgnt_books[bcv[0:2]][1], int(bcv[2:4]), int(bcv[4:6]))

def emphasizeLemmas(verse, lemmas, clr = color.CYAN):
    """Emphasize lemmas in the given verse.
    """

    return ' '.join([clr + w['text'] + color.END if w['lemma'] in lemmas else w['text'] for w in verse.morph_words])


def search(args):
    """Produce the concordance of the given lemma searching it
    in the New Testament.
    """

    for r in gnttb.search.search(args.lemma):
        print('{} : {}'.format(bcv.bcv2str(r.morph_words[0]['bcv']), emphasizeLemmas(r, [args.lemma,])))
