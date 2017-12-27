#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import argparse

parser = argparse.ArgumentParser(description='Extract some log info.')

parser.add_argument('log_folder', help='log files location')
parser.add_argument('-o', '--output', help='the output file', default='output.csv')

args = parser.parse_args()


outputFile = open(args.output, 'w')
outputFile.write('URL, TIME, SIZE\n')

for logFileName in os.listdir(args.log_folder):
    print('Processing: ' + logFileName)

    logFileData = open('data/' + logFileName, 'r')

    for line in logFileData:
        line = line.split()
        try:
            if line[3] == 'FINISH':
                parsedJson = {}
                try:
                    parsedJson =  json.loads(line[5])
                except:
                    parsedJson =  json.loads(line[5] + line[6])
                outputFile.write(line[4] + ', ' +  parsedJson['time'] + ', ' + parsedJson['size'] + '\n')
        except:
            continue

outputFile.close()
