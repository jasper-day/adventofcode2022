# day five
import re

crate1 = ["F","H","B","V","R","Q","D","P"]
crate2 = ["L","D","Z","Q","W","V"]
crate3 = ["H","L","Z","Q","G","R","P","C"]
crate4 = ["R","D","H","F","J","V","B"]
crate5 = ["Z","W","L","C"]
crate6 = ["J","R","P","N","T","G","V","M"]
crate7 = ["J","R","L","V","M","B","S"]
crate8 = ["D","P","J"]
crate9 = ["D","C","N","W","V"]

def movement(line):
    lineregex = re.compile(r"move (\d+) from (\d+) to (\d+)")
    mo = lineregex.search(line)
    return int(mo.group(1)), int(mo.group(2)), int(mo.group(3))


crates = [crate1, crate2, crate3, crate4, crate5, crate6, crate7, crate8, crate9]

puzzin = open("0502.txt", 'r')
puzzlines = puzzin.readlines()

for line in puzzlines:
    number, start, end = movement(line)
    start -= 1
    end -= 1
    for i in range(-number, 0):
        crates[end].append(crates[start].pop(i))

print("Answer to day 5:")

for crate in crates:
    print(crate[-1], end="")