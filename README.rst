Scan multiple pdf files with CanoScan LiDE 600F
===============================================
Based on the `scan script of Jürgen Ernst`_.

.. _scan script of Jürgen Ernst: http://www.juergen-ernst.de/info_sane.html 

Usage
------------
usage: scan.py [-h] [-o OUTPUT] [-p PAGES] [-b BRIGHTNESS_CONTRAST] [-c COLOR]

Scan several pages and merge them into a single pdf file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file name
  -p PAGES, --pages PAGES
                        number of pages to scan
  -b BRIGHTNESS_CONTRAST, --brightness_contrast BRIGHTNESS_CONTRAST
                        brightness contrast option for imagemagick
  -c COLOR, --color COLOR
                        colorspace option for imagemagick

example: scan.py -p 3 -o mydocument.pdf
