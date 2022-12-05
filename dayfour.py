# day four part 1

import re

puzzin = open("0401.txt")
puzzlines = puzzin.readlines()

def contains(range1, range2): 
    def checkin(range1, range2):
        # check if range 1 in range 2
        (start1, end1) = range1
        (start2, end2) = range2
        return start1 <= start2 and end1 >= end2
    return checkin(range1, range2) or checkin (range2, range1)

def ranges(line):
    rangeregex = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')
    mo = rangeregex.search(line)
    return (int(mo.group(1)), 
            int(mo.group(2))), (int(mo.group(3)), int(mo.group(4)))

total = 0

for line in puzzlines:
    range1, range2 = ranges(line)
    if contains(range1, range2):
        total += 1

print("answer to day 4:")
print(total)
    