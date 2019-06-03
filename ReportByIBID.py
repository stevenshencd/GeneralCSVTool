#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function
#
# """

# """
import os
import sys
from taas.tools.CSVResolver import CSVResolver


debug = True


class ReportByIBID(object):
    daily_report_path = ""
    base_report_path = ""
    output_report_path = ""

    def __init__(self, daily_report_path, base_report_path, output_path):
        self.daily_report_path = daily_report_path
        self.base_report_path = base_report_path
        self.output_report_path = output_path

    def write_to_csvfile(self, filename, rows):
        fp = open(filename, 'w')
        for row in rows:
            line = ""
            for v in row:
                line = line + v + ","
            line = line[0:len(line) - 1]
            line += '\n'
            fp.writelines(line)
        fp.close()

    def add_new_ibid(self):
        daily_rows = CSVResolver(self.daily_report_path).get_reader()
        i = 0
        new_report = []
        for row in daily_rows:
            if i > 0:
                new_row = self.find_row_from_base(row)
                new_row.append(row[4] + "-" + row[7])
                new_report.append(new_row)
            i += 1
        return new_report

    def update_last_ibid(self):
        daily_rows = CSVResolver(self.daily_report_path).get_reader()
        i = 0
        new_report = []
        for row in daily_rows:
            if i > 0:
                new_row = self.find_row_from_base(row)
                new_row[-1] = row[4] + "-" + row[7]
                new_report.append(new_row)
            i += 1
        return new_report

    def find_row_from_base(self, record):
        base_rows = CSVResolver(self.base_report_path).get_reader()
        l = 0
        for row in base_rows:
            if l == 1:
                blank_row = row
            l += 1
            if row[1] == record[1] and row[2] == record[2] and row[3] == record[3]:
                return row
        # for not found from base report, create new row
        blank_row[0] = "new_test"
        blank_row[1:4] = record[1:4]
        if len(blank_row) > 4:
            for i in range(4, len(blank_row) - 1):
                blank_row[i] = ""
        return blank_row

    def generate_ibid_tracking_report(self):
        if not os.path.exists(self.daily_report_path):
            print "Wrong daily report path/filename"
            return 1
        if not os.path.exists(self.base_report_path):
            print "Base report missed"
            return 2
        daily_report = CSVResolver(self.daily_report_path)
        base_report = CSVResolver(self.base_report_path)
        # get last ibid from tracking report
        head_line = base_report.get_header()
        last_ibid = head_line[-1]
        # get latest ibid from daily report
        ibid_list = daily_report.get_column_in_unique_value(7)
        # generate report data according to last_ibid
        report_rows = []
        for ibid in ibid_list:
            if ibid.isdigit():
                if int(ibid) > int(last_ibid):
                    head_line.append(ibid)
                    report_rows = self.add_new_ibid()
                    break
            elif len(ibid[ibid.rfind(".") + 1:]) == 6:
                if int(ibid[-6:]) > int(last_ibid):
                    head_line.append(ibid[-6:])
                    report_rows = self.add_new_ibid()
                    break
            # No new ibid
            report_rows = self.update_last_ibid()
        # add headline
        report_rows.insert(0, head_line)
        self.write_to_csvfile(self.output_report_path, report_rows)
        print "IBID tracking report is created successfully"
        return 0


if __name__ == '__main__':
    # debug code
    if debug:
        report = ReportByIBID("temp_data" + os.sep + "utms_running_instances.csv", "temp_data" + os.sep
                              + "Test_Result_Per_Build.csv", "report" + os.sep + "Test_Tracking_Per_Build.csv")
        report.generate_ibid_tracking_report()
    else:
        if len(sys.argv) < 4:
            print "arguments missed, python ReportByIBID.py daily_report_file, base_report_file,output_file"
            exit()
        else:
            report = ReportByIBID(sys.argv[1], sys.argv[2], sys.argv[3])
            report.generate_ibid_tracking_report()
