# Week 4 - Reg Ex
# This code will anonymise the sub domain of ip address

import re

regex = "\d{1,3}\.\d{1,3} "
replacementText = "XXX.XXX "

filename = "./smallaccess.log"
outputFileName = "anonymisedIPs.txt"

with open(filename) as inputFile: 
    with open (outputFileName, 'w') as outputFile: 
        for line in inputFile:
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)