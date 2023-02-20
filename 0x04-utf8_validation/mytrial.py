#!/usr/bin/env python3
""" a method to validate that an input is utf8 compatible """
def validUtf8(data):
    for i in data:
        numOfBytes = 0
        val = i
        print(i)
        if val >= 255:
            return 'false1'
        elif (val & 128 == 0):
            numOfBytes = 1
        elif (val & 224 == 192):
            numOfBytes = 2
        elif (val & 240 == 224):
            numOfBytes = 3
        elif (val & 248 == 240):
            numOfBytes = 4
        else:
            return 'false2'
        for j in range(numOfBytes):
            if (j+i >= len(data)):
                return 'false'
            elif (data[i+j] & 192 != 128):
                print(i)
                return 'false3'
        i = i+numOfBytes-1
        print(6)
    return 'true'

print(validUtf8([80, 121, 116, 104, 111, 110, 32, 99, 111, 111, 108, 33]))
print(validUtf8([65]))
print(validUtf8([229, 65, 127, 256]))
print(validUtf8([255]))
