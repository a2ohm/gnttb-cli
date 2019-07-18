#! /usr/bin/python3
# -*- coding:utf-8 -*-

import argparse
import sys

from sub.search import search
from sub.get import get

# Check the gnttb version
import gnttb

gnttb_neededVersion = '0.1'
if gnttb.__version__ < gnttb_neededVersion:
    print("You are using version {} of gnttb, but at least version {} is needed.".format(gnttb.__version__, gnttb_neededVersion))
    print("Please update gnttb (pip3 install --user --upgrade gnttb-a2ohm).")
    sys.exit()

# Parse arguments
parser = argparse.ArgumentParser(description="CLI of the Greek New Testament toolbox.")
subparsers = parser.add_subparsers()

# Create the parser for the 'search' command
parser_search = subparsers.add_parser('search', help='search in the New Testament')
parser_search.add_argument('lemma', help='return the concorance of lemma in the New Testament')
parser_search.set_defaults(func=search) 

# Create the parser for the 'get' command
parser_get = subparsers.add_parser('get', help='return a verse from the New Testament')
parser_get.add_argument('bcv', help='bcv of the verse')
parser_get.set_defaults(func=get) 

# Parse
args = parser.parse_args()

# Call the right module
args.func(args)
