# day 1 puzzle 1 and 2

def sanitize_line(line):
    try:
        return int(line)
    except:
        return False

with open("0101.txt", 'r'   ) as puzzle_input:
    puzzlines = [sanitize_line(line) for line in puzzle_input.readlines()]
    puzzlines.reverse()
    output = []
    count = 0
    while puzzlines != []:
        readline = puzzlines.pop()
        if readline:
            count += readline
        else:
            output.append(count)
            count = 0
    print("answer to part 1:")
    print(max(output))

sums = 0
for i in range(0,3):
    sums += max(output)
    output.remove(max(output))
print("answer to part 2:")
print(sums)