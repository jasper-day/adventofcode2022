import re
import numpy as np

PRINT_FLAG = False

puzzin = open("0901.txt")
puzzlines = puzzin.readlines()

def parse_line(line):
    linereg = re.compile(r"(\w) (\d+)")
    mo = linereg.search(line)
    return mo.group(1), int(mo.group(2))


class Ropebridge():
    def __init__(self):
        self.head = np.array([0,0])
        self.tail = [np.array([0,0]) for i in range(9)]
        self.right = np.array([1,0])
        self.up = np.array([0,1])
        self.diag = np.array([1,1])
        self.locs = []
        if PRINT_FLAG:
            self.pprint()

    def move_head(self, direction):
        if direction == "R":
            self.head += self.right
        elif direction == "L":
            self.head -= self.right
        elif direction == "U":
            self.head += self.up
        elif direction == "D":
            self.head -= self.up
    
    def move_tail(self, head, tail):
        diff = head - tail
        if abs(diff).max() > 1: # more than one step apart
                # print(f"separated by {diff}")
                tail += np.sign(diff) # move one step in the direction of the head
        #  # not in same row / column
        #     # tail moves diagonally one step to keep up unless touching
        # elif not np.array_equal(abs(diff),self.diag): # not touching diagonally
        #     # print(f"separated by {diff}")
        #     self.tail += np.sign(diff)

    def move_self(self, direction, amount):
        for i in range(amount):
            self.move_head(direction)
            # self.pprint()
            self.move_tail(self.head, self.tail[0])
            for i in range(8):
                self.move_tail(self.tail[i], self.tail[i + 1])
            if PRINT_FLAG:
                self.pprint()
            # print(f"head: {self.head}, tail: {self.tail}")
            if self.tail[8].tolist() not in self.locs:
                self.locs.append(self.tail[8].tolist())
            if PRINT_FLAG:
                print(self.locs)

    def pprint(self):
        for j in np.arange(8,-8,-1): # cols
            for i in np.arange(-8,8): # rows
                if np.array_equal(self.head, np.array([i,j])):
                    print(" H ", end="")
                elif np.array_equal(self.tail, np.array([i,j])):
                    print(" T ", end="")
                elif i ==0 and j==0:
                    print(" s ", end="")
                elif [i,j] in self.locs:
                    print(" # ", end="")
                else:
                    print(" . ", end="")
            print("")
        print("")
                

bridge = Ropebridge()

for line in puzzlines:
    line = line.strip()
    if PRINT_FLAG:
        print(f"== {line} ==")
    direction, amount = parse_line(line)
    bridge.move_self(direction, amount)


print("Answer to day 9:")
bridge.pprint()
print(len(bridge.locs))
