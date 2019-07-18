#! /usr/bin/python3
# -*- coding:utf-8 -*-

import argparse

from sub.search import search

# Parse arguments
parser = argparse.ArgumentParser(description="CLI of the Greek New Testament toolbox.")
subparsers = parser.add_subparsers()

# Create the parser for the 'search' command
parser_search = subparsers.add_parser('search', help='search in the New Testament')
parser_search.add_argument('lemma', help='return the concorance of lemma in the New Testament')
parser_search.set_defaults(func=search) 

# Parse
args = parser.parse_args()

# Call the right module
args.func(args)
