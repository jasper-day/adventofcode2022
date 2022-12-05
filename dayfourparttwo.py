# day four part 1

from dayfour import ranges

puzzin = open("0401.txt")
puzzlines = puzzin.readlines()

def overlaps(range1, range2):
    def inside(number, range1):
        start, end = range1
        return start <= number <= end
    start1, end1 = range1
    start2, end2 = range2
    return inside(start1, range2) or inside(start2, range1)



total = 0

for line in puzzlines:
    range1, range2 = ranges(line)
    if overlaps(range1, range2):
        total += 1

print("answer to day 4:")
print(total)
    