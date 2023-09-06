#!/usr/bin/python3
def uppercase(str):
    output = ""
    for ch in str:
        if ch in 'abcdefghijklmnopqrstuvwxyz':
            a = ord(ch)
            b = a - 32
            output = output+chr(b)
        else:
            output = output+ch
    print("{}".format(output))
