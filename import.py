#! /usr/bin/env python

import sys
import csv
from subprocess import Popen, PIPE

def import_entry(title, pw):
    """ Import new password entry to password-store using pass insert command """
    proc = Popen(['pass', 'insert', '--multiline', title], stdin=PIPE, stdout=PIPE)
    proc.communicate(pw.encode('utf8'))
    proc.wait()


def readcsv(filename, dlim):
    ifile = open(filename, "r")
    reader = csv.reader(ifile, delimiter=dlim)

    rownum = 0
    a = []

    for row in reader:
        a.append (row)
        rownum += 1

    ifile.close()
    return a

def main(csv_file):
    """ Parse given CSV file and import passwords from it """
    pws = readcsv(csv_file, '|')
    for entry in pws:
        print ('Inserting entry: ' + entry[0])
        import_entry(entry[0], entry[1])

if __name__ == '__main__':
    main(sys.argv[1])
