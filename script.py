#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

outputFile = open('output.csv', 'w')
outputFile.write('URL, TIME, SIZE\n')

for logFileName in os.listdir('data'):
    print('Processing: ' + logFileName)

    logFileData = open('data/' + logFileName, 'r')

    for line in logFileData:
        line = line.split()
        try:
            if line[3] == 'FINISH':
                parsedJson =  json.loads(line[5])
                print(line[4], parsedJson['time'], parsedJson['size'])
                try:
                    outputFile.write(line[4] + ', ' +  parsedJson['time'] + ', ' + parsedJson['size'] + '\n')
                except error:
                    print('error')
        except:
            continue

outputFile.close()
