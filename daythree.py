# day 3

puzzin = open("0301.txt", 'r')

puzzlines = puzzin.readlines()

def find_common(line1, line2):
    for item in line1:
        if item in line2:
            return item
def priority(character):
    ordinal = ord(character)
    if ordinal - ord('a') > 0:
        return ordinal - ord('a') + 1
    else:
        return ordinal - ord('A') + 27
     
def separate_rucksack(line):
    halfway_point = int(len(line) / 2)
    return (line[:halfway_point], line[halfway_point:])

total = 0

for line in puzzlines:
    first, last = separate_rucksack(line)
    letter = find_common(first, last)
    total += priority(letter)

print("Answer to day 3:")
print(total)