#!/usr/bin/env python


import sys
import re
#sys.stderr.write("reporter:counter:Tokens,Total,1") # NOTE missing the carriage return so wont work
sys.stderr.write("reporter:counter:Mapper Counters,Calls,1\n")
sys.stderr.write("reporter:status:processing my message...how are  you\n")

for line in sys.stdin:
    line= re.findall(r'[a-z]+', line.lower())
    line=" ".join(line)
    words = line.split()
    for word in words:
        val=len(word)
        print '%s\t%s' % (word, val)