#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ====================================================================
#  com-analysis.py
#    A center of mass testing script for typeface glyph shape analysis
#
#   Copyright 2018 Christopher Simpkins
#   MIT License
# ====================================================================

import os
import sys

from fontTools.pens.statisticsPen import StatisticsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Scale
from fontTools.ttLib import TTFont

def main(argv):
    if len(argv) != 2:
        sys.stderr.write("Please enter paths to two font files for center of mass comparisons" + os.linesep)
        sys.exit(1)

    test_glyphs = ('uni002B', 'uni002E')

    font1 = TTFont(argv[0])
    font2 = TTFont(argv[1])

    test_fonts = (font1, font2)

    for glyph_name in test_glyphs:
        print("\nGLYPH: " + glyph_name)
        x = 0
        for font in test_fonts:
            x += 1
            print("Font " + str(x))
            this_glyphset = font.getGlyphSet()
            glyph_obj = this_glyphset[glyph_name]
            stats_pen = StatisticsPen(glyphset=this_glyphset)
            upem = font['head'].unitsPerEm
            transformer = TransformPen(stats_pen, Scale(1./upem))
            glyph_obj.draw(transformer)
            
            for item in ['area', 'meanX', 'meanY']:
                print("%s: %g" % (item, getattr(stats_pen, item)))
            
            print(" ")

        print(" ")


if __name__ == '__main__':
    main(sys.argv[1:])
