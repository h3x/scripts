#!/usr/bin/python3
import sys
import codecs
text = sys.stdin.read()
print(codecs.encode(text, 'rot_13'))
