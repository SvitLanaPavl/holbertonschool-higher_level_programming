#!/usr/bin/python3
import sys

if (len(sys.argv) - 1) == 0:
    print("0 arguments.")
else:
    if (len(sys.argv) - 1) == 1:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
