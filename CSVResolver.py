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


class CSVResolver():
    fp = ""
    def __init__(self, filename):
        if os.path.exists(filename):
            try:
                self.fp = open(filename,"r")
            except IOError:
                print "Open csv file error"
        else:
            print "The file doesn't exist"

    def get_column(self, index):
        self.fp.seek(0)
        reader = csv.reader(self.fp)
        return [row[index] for row in reader]

    def get_value(self, row, col):
        self.ft.seek(0)
        reader = csv.reader(self.fp)
        for i, line in enumerate(reader):
            if i == row:
                return line[col]

    def get_column_unique_values(self, index):
        self.fp.seek(0)
        reader = csv.reader(self.fp)
        return list(set(self.get_column(index)))


    def get_header(self):
        self.fp.seek(0)
        reader = csv.reader(self.fp)
        for i, row in enumerate(reader):
            if i == 0:
                return row
            else:
                break

    def get_column_equals_content(self,col_index, filter_index, filter_content):
        self.fp.seek(0)
        reader = csv.reader(self.fp)
        return [row[col_index] for row in reader if row[filter_index] == filter_content]

    def get_rows_by_filter(self,filter):
        self.fp.seek(0)
        reader = csv.reader(self.fp)
        rows = []
        for row in reader:
            if filter(row) == 0:
                rows.append(row)
        return rows

if __name__ == '__main__':
    # debug code
    print "run..."
    resolver = CSVResolver("debug/instance_all.csv")
    def filter_age(row):
        return 0
    print resolver.get_rows_by_filter(filter_age)


