#!/usr/bin/env python
file = open('list.txt','r')

with file as f:
    i = 0
    prevline = ""

    for line in f:
        line = line.strip()
        channelNumber = str(int(i / 2) + 1)

        if i % 2 == 0:
            diff = ""
        else:
            diff = "adress"

        fine = "channel" + diff + channelNumber + "=" + line
        print(fine)

        i = i + 1

        isDVR = line.strip()[-4:].lower()
        if isDVR == "?dvr":
            channelNumber = str(int(i / 2) + 1)
            i = i + 2

            fine1 = "channel" + channelNumber + "=" + prevline + " 2"
            fine2 = "channeladress" + channelNumber + "=" + line[:-4]
            print (fine1)
            print (fine2)

        prevline = line
