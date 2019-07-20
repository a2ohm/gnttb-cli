#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the get sub-command.
"""

import gnttb.compare

from tools import bcv
from tools.colors import colors

def compare(args):
    """Compare two verses given their bcv.
    """

    fg_emph = colors.fg.PINK
    bg_emph = colors.bg.PINK

    verse1 = gnttb.get.get(args.bcv1)
    verse2 = gnttb.get.get(args.bcv2)

    averse1, averse2 = gnttb.compare.compare(verse1, verse2)

    # Display the comparaison in columns
    colWidth = 42
    buffSize = 0
    buff1 = ""
    buff2 = ""

    isUsingColor = 0    # 0: no, 1: fg, 2: bg

    print(" {c_emph}{:^{width}}{c_end} | {c_emph}{:^{width}}{c_end}".format(bcv.bcv2str(verse1.bcv), bcv.bcv2str(verse2.bcv),
        c_emph = colors.BOLD, c_end = colors.END, width = colWidth))

    for w1, w2 in zip(averse1, averse2):
        ww1 = "" if w1 is None else w1['text']
        ww2 = "" if w2 is None else w2['text']

        wSize = max(len(ww1), len(ww2))

        if buffSize + wSize + 1 > 42:
            # News words do not fit in width.
            # So display current buffers and reset them
            # to create a new line.

            # Properly end text formating
            if isUsingColor > 0:
                buff1 += colors.END
                buff2 += colors.END
                isUsingColor = 0

            # Display buffers
            print(" {}{} | {}".format(buff1, ' '*(colWidth-buffSize), buff2))

            # and reset them
            buff1 = ""
            buff2 = ""
            buffSize = 0

        # Format text
        if w1 is not None and w2 is not None:
            if w1['norm'] == w2['norm']:
                # Same word: strong emphasis
                if isUsingColor == 0:
                    isUsingColor = 2
                    ww1 = "{{space}}{}{:{width}}".format(bg_emph, ww1, width = wSize)
                    ww2 = "{{space}}{}{:{width}}".format(bg_emph, ww2, width = wSize)

                elif isUsingColor == 1:
                    isUsingColor = 2
                    ww1 = "{}{{space}}{}{:{width}}".format(colors.END, bg_emph, ww1, width = wSize)
                    ww2 = "{}{{space}}{}{:{width}}".format(colors.END, bg_emph, ww2, width = wSize)

                else:
                    ww1 = "{{space}}{:{width}}".format(ww1, width = wSize)
                    ww2 = "{{space}}{:{width}}".format(ww2, width = wSize)

            elif w1['lemma'] == w2['lemma']:
                # Same lemma: light emphasis
                if isUsingColor == 0:
                    isUsingColor = 1
                    ww1 = "{{space}}{}{:{width}}".format(fg_emph, ww1, width = wSize)
                    ww2 = "{{space}}{}{:{width}}".format(fg_emph, ww2, width = wSize)

                elif isUsingColor == 2:
                    isUsingColor = 1
                    ww1 = "{}{{space}}{}{:{width}}".format(colors.END, fg_emph, ww1, width = wSize)
                    ww2 = "{}{{space}}{}{:{width}}".format(colors.END, fg_emph, ww2, width = wSize)

                else:
                    ww1 = "{{space}}{:{width}}".format(ww1, width = wSize)
                    ww2 = "{{space}}{:{width}}".format(ww2, width = wSize)
            else:
                if isUsingColor > 0:
                    isUsingColor = 0
                    ww1 = "{}{{space}}{:{width}}".format(colors.END, ww1, width = wSize)
                    ww2 = "{}{{space}}{:{width}}".format(colors.END, ww2, width = wSize)
                else:
                    ww1 = "{{space}}{:{width}}".format(ww1, width = wSize)
                    ww2 = "{{space}}{:{width}}".format(ww2, width = wSize)

        else:
            if isUsingColor > 0:
                isUsingColor = 0
                ww1 = "{}{{space}}{:{width}}".format(colors.END, ww1, width = wSize)
                ww2 = "{}{{space}}{:{width}}".format(colors.END, ww2, width = wSize)
            else:
                ww1 = "{{space}}{:{width}}".format(ww1, width = wSize)
                ww2 = "{{space}}{:{width}}".format(ww2, width = wSize)

        # Append words to their buffer
        # adding a space if necessary
        if buffSize == 0:
            buff1 += ww1.format(space = '')
            buff2 += ww2.format(space = '')
            buffSize += wSize
        else:
            buff1 += ww1.format(space = ' ')
            buff2 += ww2.format(space = ' ')
            buffSize += wSize + 1


    # Print the last line
    # Properly end text formating
    if isUsingColor > 0:
        buff1 += colors.END
        buff2 += colors.END

    # Display buffers
    print(" {}{} | {}".format(buff1, ' '*(colWidth-buffSize), buff2))
