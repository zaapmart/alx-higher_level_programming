#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char

    if result:
        print("{}".format(result))
