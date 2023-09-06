#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[slice(39,65)] + " " + str[slice(-21, -18)] + " " + str[slice(0, 5)]
print(str)