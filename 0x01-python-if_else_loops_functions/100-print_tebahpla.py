#!/usr/bin/python3
for alph in range(ord('z'), ord('a') -1, -2):
    print("{}{}".format(chr(alph), chr(alph - 33)), end='')
