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
    if os.path.exists("report"):
        print "maybe need to clean datafiles"
    else:
        os.mkdir("report")

def extract_all_run_instance(root_folder):
    print "if over 5, then only get last 5 instances"

def generate_report(rows):
    print "generate report"
    report_name = "report_{date}".format(date=time.strftime("%Y/%m/%d"))

def filter_timeline_after(row):
    str_date = str(row[3]).split(" ")[0]
    try:
        executed_date = datetime.datetime.strptime(str_date, '%Y/%m/%d').date()
    except Exception:
        print ""
    if executed_date >= datetime.datetime.strptime("2019/3/20", '%Y/%m/%d').date():
        return 0
    else:
        return -1

def main():
    if len(sys.argv) < 2 & False:
        print "please input parameters: root_folder and timeline, e.g. python ExecutionReport --rootfolder folder_path --timeline 2019/3/18"
        exit()
    clean()
    extract_all_run_instance("Xian") #get all instance for all test cases under root folder
    time.sleep(3)
    try:
        resolver = CSVResolver("temp_data" + os.sep + "all_instances_{date}".format(date=time.strftime("%Y/%m/%d")))
    except Exception:
        print Exception

    rows = [["Itag", "Category", "TestName", "Status", "Last_5_Pass_Rate", "Latest_Execution_Date","Note"]]

    print "done"

if __name__ == '__main__':
    # debug code
    print "ExecutionReport"
    main()