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
from CSVResolver import CSVResolver
from utilities import write_to_csvfile


debug = True
data_folder = ""


def clean():
    if os.path.exists(data_folder):
        for f in os.listdir(data_folder):
            print f
    else:
        os.mkdir(data_folder)


def merge_sign_data(input):
    pass


def merge_machine_data(input):
    pass


def main():
    pass

if __name__ == '__main__':

    # for not found from base report, create new row
    if debug:
        data_folder += "C:\\github\\data\\counter"
        clean()
