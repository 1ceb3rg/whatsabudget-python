
from datetime import datetime
from dateutil.relativedelta import *
import sys
from dateutil.parser import *
import re
import argparse

defaultStart = '01/01/1990'
defaultEnd = str(datetime.now())


class Budget:
    items = {}
    def __init__(self, items={}):
        if items:
            self.items = items

    def getCurrent(self, startDate, endDate):
        totals = {}
        for person in self.items.keys():
            totals[person] = 0
            for row in self.items[person]:
                rowDate = parse(row[0])
                if(parse(startDate) <= rowDate and rowDate <= parse(endDate)):
                    totals[person] += float(row[1])
        for person in totals.keys():
            print(f'{person}: {totals[person]:.2f}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Whatsapp chat log budget parser")
    parser.add_argument('filename', help='.txt file from the exported chat')
    parser.add_argument(
        '--startDate', help='the date to start calculating from', default=defaultStart)
    parser.add_argument(
        '--endDate', help='the date to stop calculating at', default=defaultEnd)
    args = parser.parse_args()
try:
    file = open(args.filename, 'r')
except:
    print('cannot open file')
    raise SystemExit

reg = re.compile('\[(.*)\]\s([^:]*):\s(.*)')
items = {}
totals = {}
for line in file.readlines():
    parsedLine = reg.match(line)
    if parsedLine:
        data = parsedLine.groups()
        try:
            float(parsedLine.groups()[2])

            if data[1] not in items.keys():
                items[data[1]] = []
            items[data[1]].append([data[0], data[2]])
        except Exception as ex:
            ex

currentBudget = Budget(items)
currentBudget.getCurrent(args.startDate, args.endDate)
