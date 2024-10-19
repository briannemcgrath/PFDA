# Week 4 - Reg Ex
# This code will find some text in an access file

import re

regex = "\[.*\]"
filename = "./smallaccess.log"

with open(filename) as inputFile: 
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList) != 0):
            #print (foundTextList)
            foundText = foundTextList [0]
            #print(foundText)
            # if yuou did not want the [] at the beginng and end 
            print(foundText[1:-1])

