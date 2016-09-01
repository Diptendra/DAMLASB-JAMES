#!/usr/bin/env python

import sys
import re
cur_key = None
cur_length = 0
sys.stderr.write("reporter:counter:Reducer Counters,Calls,1\n")
for line in sys.stdin:
    key, value = line.split()
    if key == cur_key:
        cur_length = int(value)
    else:
        if cur_key:
            if cur_length > int(value):
                cur_key=cur_key
                cur_length=cur_length
            else:
                cur_key = key
                cur_length = int(value)
        else:
            cur_key = key
            cur_length = int(value)
            
print '%s\t%s' % (cur_key, cur_length)