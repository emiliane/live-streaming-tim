#!/usr/bin/env python
file = open('list.txt','r')

i = 0
with file as f:
    for line in f:
        channelNumber = str(int(i / 2) + 1)
        if i % 2 == 0:
            print ("channel" + channelNumber + "=" + line   , end = '')
        else:
            print ("channeladress" + channelNumber + "=" + line   , end = '')
        i = i + 1
