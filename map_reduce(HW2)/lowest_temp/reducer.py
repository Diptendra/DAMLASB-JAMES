#!/usr/bin/env python

import sys
import re
min_temp = 0.0
final_key = None
sys.stderr.write("reporter:counter:Reducer Counters,Calls,1\n")
for line in sys.stdin:
    key, value = line.split()
    if key == final_key:
        if float(value) > min_temp:
            min_temp = min_temp
        else:
            min_temp = value
    else:
        if final_key:
            if float(value) > min_temp:
                min_temp = min_temp
            else:
                min_temp = float(value)
                final_key = key
        else:
            final_key = key
            min_temp = float(value)

print '%s\t%s' % (final_key, min_temp)