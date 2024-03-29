#! /usr/bin/python3
# -*- coding:utf-8 -*-

import argparse
import sys

from sub.compare import compare
from sub.get import get
from sub.search import search

# Check the gnttb version
import gnttb

gnttb_neededVersion = '1.2'
if gnttb.__version__ < gnttb_neededVersion:
    print("You are using version {} of gnttb, but at least version {} is needed.".format(gnttb.__version__, gnttb_neededVersion))
    print("Please update gnttb (see its documentation at https://github.com/a2ohm/gnttb).")
    sys.exit()

about_bcv = "Notice: learn about bcv in the README.md file."

# Parse arguments
parser = argparse.ArgumentParser(description="CLI of the Greek New Testament toolbox.")
subparsers = parser.add_subparsers()

# Create the parser for the 'compare' command
parser_compare = subparsers.add_parser('compare', help='compare two groups of verses', epilog=about_bcv)
parser_compare.add_argument('bcv1', help='bcv of the first group of verses')
parser_compare.add_argument('bcv2', help='bcv of the second group of verses')
parser_compare.set_defaults(func=compare) 

# Create the parser for the 'get' command
parser_get = subparsers.add_parser('get', help='return a group of verses from the New Testament', epilog=about_bcv)
parser_get.add_argument('bcv', help='bcv of the group of verses')
parser_get.set_defaults(func=get) 

# Create the parser for the 'search' command
parser_search = subparsers.add_parser('search',
        help='search in the New Testament',
        epilog='Notice: see examples of the search command in the README.md file.')
parser_search.add_argument('--book', '-b', dest='books', default=[], action='append', help='limit the search to some books given their ids')
parser_search.add_argument('--ccatParse', default='', help='filter result with a parsing code')
parser_search.add_argument('lemma', help='return the concorance of lemma in the New Testament')
parser_search.set_defaults(func=search) 

# Parse
args = parser.parse_args()

# Call the right module
args.func(args)
