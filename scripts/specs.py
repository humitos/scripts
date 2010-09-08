#!/usr/bin/python
import sys
import re
from subprocess import Popen, PIPE
import os

filename = sys.argv[1]
output = Popen(['python', filename], stdout=PIPE).stdout.read()
r = re.search(r'\*\*\*Test Failed\*\*\* (?P<fail>\d+) failures.', output)
if r:
    fails = r.group('fail')
    if fails:
        print output
        cmd = 'aosd_cat Test Failed: %s -r 255 -g 0 -b 0' % fails
else:
    cmd = 'aosd_cat All Test Passed -r 0 -g 255 -b 0'
os.system(cmd)
