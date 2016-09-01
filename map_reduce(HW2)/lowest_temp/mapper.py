#!/usr/bin/env python


import sys
import re
#sys.stderr.write("reporter:counter:Tokens,Total,1") # NOTE missing the carriage return so wont work
sys.stderr.write("reporter:counter:Mapper Counters,Calls,1\n")
sys.stderr.write("reporter:status:processing my message...how are  you\n")

for line in sys.stdin:
    line= re.findall(r'[0-9.]+', line)
    if line != []:
        #words = line.split()
        #line = line.strip()
        if (len(line[0]) == 4 and 1 <= int(line[1]) <= 12):
            print '%s\t%s' % (line[0], line[3])  