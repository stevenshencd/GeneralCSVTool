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

    def get_column_with_filter(self,col_index, filter_index, filter_content):
        self.fp.seek(0)
        reader = csv.reader(self.fp)
        return [row[col_index] for row in reader]

    def get_rows_by_timeline(self,mode,filter_column_index,timeline):
        self.fp.seek(0)
        reader = csv.reader(self.fp)
        rows_before = []
        rows_after = []
        i = 0
        for row in reader:
            if i > 0:
                str_date = str(row[filter_column_index]).split(" ")[0]
                try:
                    executed_date = datetime.datetime.strptime(str_date,'%Y/%m/%d').date()
                    if datetime.datetime.strptime(timeline,'%Y/%m/%d').date() > executed_date:
                        rows_before.append(row)
                    else:
                        rows_after.append(row)
                except:
                    continue
            i += 1
        if mode.lower() == "before":
            return rows_before
        else:
            return rows_after

if __name__ == '__main__':
    # debug code
    print "run..."
    resolver = CSVResolver("debug/instance_all.csv")
    print resolver.get_header()
    print resolver.get_rows_by_timeline("Before",8,"2019/3/2")
