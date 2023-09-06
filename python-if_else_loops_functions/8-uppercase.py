#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ch in 'abcdefghijklmnopqrstuvwxyz':
            a = ord(ch)
            b = a - 32
    print("{}".format(chr(b)))
    