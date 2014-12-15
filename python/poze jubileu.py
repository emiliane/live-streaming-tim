#!/usr/bin/python
import subprocess, os

first = 2
last = 244
address = 'http://www.betel.ro/wp-content/uploads/2014/01/Jubileu-Betel-2013-'
for i in range(first, last):
    addressNew = address + str(i) + '.jpg'
    commnad = 'curl ' + addressNew + ' --> ' + str(i).zfill(3) + '.jpg'
    print (commnad)
    subprocess.call(commnad, shell = True)
