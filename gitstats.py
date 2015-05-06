#!/usr/bin/env python

import urllib
from lxml import etree
import sys
try:
    from dateutil import parser
except ImportError:
    from bdateutil import parser

def main(username):
    url = "https://github.com/users/%s/contributions" % username
    t = etree.parse(urllib.urlopen(url))
    weeknames = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_dict = {weeknames[i]: 0 for i in range(7)}
    for entry in t.xpath('//rect [@data-date]'):
        weekday = parser.parse(entry.get('data-date')).weekday()
        days_dict[weeknames[weekday]] += int(entry.get('data-count'))
    for i in range(7):
        print("%-9s %d" % (weeknames[i], days_dict[weeknames[i]]))

if __name__ == '__main__':
    main(username=sys.argv[1])
