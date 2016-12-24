#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: https://chenjiehua.me
# @date: 2016-12-24
#

"""
Usage:
    python main.py a.png
"""

import sys
import numpy as np
from PIL import Image


def main():
    img_file = sys.argv[1]
    img = Image.open(img_file)
    w, h = img.size
    for y in range(h):
        line = []
        for x in range(w):
            pix = img.getpixel((x, y))
            pix = (pix[0]*299+pix[1]*587+pix[2]*114)/1000   # gray
            line.append(pix)

        lmean, lvar = np.mean(line), np.var(line)
        print lmean, lvar
        if 40 < lmean and lmean < 70 and lvar < 500:
            fix_row(img, y, y-4)

    img.save("out_" + img_file)


def fix_row(img, drt, src):
    print "fix row: %s with %s" % (drt, src)
    w, h = img.size
    if 0 <= drt and drt < h and 0 <= src and src < h:
        for x in range(w):
            img.putpixel((x, drt), img.getpixel((x, src)))


if __name__ == "__main__":
    main()
