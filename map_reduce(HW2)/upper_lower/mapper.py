#!/usr/bin/env python


import sys
import re
#sys.stderr.write("reporter:counter:Tokens,Total,1") # NOTE missing the carriage return so wont work
sys.stderr.write("reporter:counter:Mapper Counters,Calls,1\n")
sys.stderr.write("reporter:status:processing my message...how are  you\n")

for line in sys.stdin:
    line= re.findall(r'[a-zA-Z]+', line)
    line=" ".join(line)
    words = line.split()
    for word in words:
        if word[0].isupper()==True:
            case='uppercase'
            print '%s\t%s\t%s' % (word,1,case)
        else:
            case='lowercase'
            print '%s\t%s\t%s' % (word,1,case)