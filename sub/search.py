#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the search sub-command.
"""

import gnttb.search
import gnttb.sblgnt

from tools import bcv
from tools import colors

def emphasizeLemmas(verse, lemmas, clr = colors.colors.CYAN):
    """Emphasize lemmas in the given verse.
    """

    return ' '.join([clr + w['text'] + colors.colors.END if w['lemma'] in lemmas else w['text'] for w in verse.morph_words])


def search(args):
    """Produce the concordance of the given lemma searching it
    in the New Testament.
    """

    for r in gnttb.search.search(args.lemma):
        print('{} : {}'.format(bcv.bcv2str(r.morph_words[0]['bcv']), emphasizeLemmas(r, [args.lemma,])))
