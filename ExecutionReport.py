#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function
#
# """
# This is a general class to provide functions for text file analysis and report.
# """
import csv
import os
import datetime
import sys
import time

from CSVResolver import *

def clean():
    print "clean data"

def extract_run_instance():
    print

def generate_report():
    print "generate report"

def main():
    if len(sys.argv) < 2 & False:
        print "please input parameters: root_folder and timeline, e.g. python ExecutionReport --rootfolder folder_path --timeline 2019/3/18"
        exit()

    clean()
    extract_run_instance()

    print "report_{date}".format(date = time.ctime())
    print "done"



if __name__ == '__main__':
    # debug code
    print "ExecutionReport"
    main()