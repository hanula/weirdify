# -*- encoding: utf-8 -*-

import os
import sys
import random
import unicodedata
import collections


WEIRDNESS = 18
conversions = collections.defaultdict(list)
input_chars = [chr(i) for i in range(ord('z') + 1, WEIRDNESS * 1000)]


def normalize(char):
    return unicodedata.normalize('NFKD', char)


for char in input_chars:
    n = normalize(char)
    if n:
        conversions[n].append(char)


def convert(text):
    return ''.join([random.choice(conversions.get(c, [c])) for c in text])


def usage():
    print('Usage: {} "[Text to convert]"'.format(sys.argv[0]))
    sys.exit(os.EX_USAGE)


if len(sys.argv) < 2:
    usage()
else:
    text = ' '.join(sys.argv[1:])
    print(convert(text))
