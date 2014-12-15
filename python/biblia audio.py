#!/usr/bin/python
import subprocess, os
'''
numberBooksFrom = 3
numberBooksTo = 66
numberChapters = 99
test = 'http://pote.ca/dan/66/14.mp3'
address = 'http://pote.ca/dan/'

for numberBook in range (numberBooksFrom, numberBooksTo + 1):
    for numberChapter in range (1, numberChapters + 1):
        addressNew = address + str(numberBook).zfill(2) + '/' + str(numberChapter).zfill(2) + '.mp3'
        command = 'curl ' + addressNew + ' --> ' + str(numberBook).zfill(2) + '.' + str(numberChapter).zfill(2) + '.mp3'
        subprocess.call('curl ' + addressNew + ' --> ' + str(numberBook).zfill(2) + '.' + str(numberChapter).zfill(2) + '.mp3', shell = True)


'''

a = os.listdir('../audio')
a.pop(0)

carte = 1
total = 0
for b in a:
    c = b[:2]
    if (c != str(carte).zfill(2)):
        print (total)
        carte = carte + 1
        total = 0
    total = total + 1
print (total)
