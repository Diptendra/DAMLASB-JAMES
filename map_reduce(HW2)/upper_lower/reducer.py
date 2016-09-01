#!/usr/bin/env python

import sys
import re
upper_key = None
lower_key = None
upper_count = 0
lower_count = 0
sys.stderr.write("reporter:counter:Reducer Counters,Calls,1\n")
for line in sys.stdin:
    key, value, case = line.split()
    if case =='uppercase':
        if key == upper_key:
            upper_count = upper_count
        else:
            if upper_key:
                upper_key = key
                upper_count = upper_count+1
            else:
                upper_key = key
                upper_count = int(value)
    else:
        if key == lower_key:
            lower_count = lower_count
        else:
            if lower_key:
                lower_key = key
                lower_count = lower_count+1
            else:
                lower_key = key
                lower_count = int(value)

print '%s\t%s' % ('lowercase_words', lower_count)
print '%s\t%s' % ('uppercase_words', upper_count)