# day 3 part 2

puzzin = open("0301.txt", 'r')

puzzlines = puzzin.readlines()

def find_common(line1, line2, line3):
    for item in line1:
        if item in line2 and item in line3:
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

for i in range(0,int(len(puzzlines)/3)):
    index = 3 * i
    letter = find_common(puzzlines[index], puzzlines[index + 1], puzzlines[index + 2])
    total += priority(letter)


print("Answer to day 3 part 2:")
print(total)