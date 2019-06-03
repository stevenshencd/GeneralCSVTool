#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function
#
# """

# """
import os
import sys


debug = True


def write_to_csvfile(filename, rows):
    fp = open(filename, 'w')
    for row in rows:
        line = ""
        for v in row:
            line = line + v + ","
        line = line[0:len(line) - 1]
        line += '\n'
        fp.writelines(line)
    fp.close()




if __name__ == '__main__':
    # debug code
    if debug:
        pass
