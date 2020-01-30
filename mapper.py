#!/usr/bin/env python
import sys
import string


stopwords = set(['the','and'])

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()

    # removing punctuation
    exclude = set(string.punctuation)
    line = ''.join(ch for ch in line if ch not in exclude)

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords:
            print '%s\t%s' % (word, "1")
