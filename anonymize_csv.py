#!/usr/bin/env python3
from __future__ import print_function
import sys
import csv
import itertools

def pseudonym_for(x, _state=itertools.count(1), _d={}):
    if x in _d:
        return _d[x]
    else:
        r = _d[x] = next(_state)
        return r

def anonymize(row, colname):
    try:
        row[colname] = pseudonym_for(row[colname])
        return row
    except KeyError:
        print("Column %s does not exist" % colname, file=sys.stderr)
        sys.exit(1)

def main(filename, colname):
    with open(filename, 'r') as infile:
        r = csv.DictReader(infile)
        w = csv.DictWriter(sys.stdout, r.fieldnames)
        w.writeheader()
        lines = (anonymize(row, colname) for row in r)
        for line in lines:
            w.writerow(line)

if __name__ == '__main__':
    try:
        main(*sys.argv[1:])
    except TypeError:
        print("Usage: python anonymize_csv.py [filename] [column name to anonymize] > [output_filename]",
              file=sys.stderr)
        
