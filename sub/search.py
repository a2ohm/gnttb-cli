#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the search sub-command.
"""

import gnttb.search
import gnttb.sblgnt

from tools import bcv
from tools.colors import colors

def emphasizeLemmas(verse, lemmas, clr = colors.fg.CYAN):
    """Emphasize lemmas in the given verse.
    """

    return ' '.join([clr + w['text'] + colors.END if w['lemma'] in lemmas else w['text'] for w in verse.morph_words])


def search(args):
    """Produce the concordance of the given lemma searching it
    in the New Testament.
    """

    for book_num, verses in gnttb.search.search(args.lemma):
        print('{} ({} verse{})'.format(getattr(gnttb.sblgnt.sblgnt_books[book_num], 'BJ'), len(verses), 's' if len(verses) > 1 else ''))
        print('---')

        for v in verses:
            print('{} : {}'.format(bcv.bcv2str(v.morph_words[0]['bcv']), emphasizeLemmas(v, [args.lemma,])))

        print()
