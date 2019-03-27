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

def inquiry_recent_instances(name,max_count,collection):
    #inquiry each test case recent run instances in current PSI, pass rate, latest status, last execution data, note


def generate_report(rows):
    print "generate report"
    report_name = "report_{date}".format(date=time.strftime("%Y/%m/%d"))

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
    new_run_instances = resolver.get_rows_by_timeline("2019/3/20")
    inquiry_recent_instances("name",5,new_run_instances)
    rows = [["Itag", "Category", "TestName", "Status", "Last_5_Pass_Rate", "Latest_Execution_Date","Note"]]
    for test in regression_set:
        print test

    for test in ctag_set:
        print "ctag"

    print "done"

if __name__ == '__main__':
    # debug code
    print "ExecutionReport"
    main()