# Day 10 
import re
import numpy as np

puzzin = open("1001.txt")
puzzlines = puzzin.readlines()


def parse_line(line):
    linere = re.compile(r"(noop|addx )(-?\d+)?")
    mo = linere.search(line)
    if mo.group(2):
        return mo.group(1), int(mo.group(2))
    else:
        return mo.group(1), 0


        

class CPU():
    def __init__(self):
        self.cycle = 1
        self.interesting = np.arange(20,221,40)
        self.x = 1
        self.sumsig = 0
        self.screen = np.zeros([6,40]).flatten() # 6 rows, 40 columns

    def sprite(self):
        return np.arange(self.x - 1, self.x + 2)

    def inc_cyc(self):
        if self.cycle in self.interesting:
            # print(f"X register at cycle {self.cycle}: {self.x}")
            self.sumsig += self.cycle * self.x
        if (self.cycle - 1)%40 in self.sprite():
            # print(f"screen printed at cycle {self.cycle}")
            self.screen[self.cycle - 1] = 1.0
        self.cycle += 1
    def addx(self, num):
        self.x += num
    def pretty_print(self):
        for j in range(0,6):
            for i in range(0,40):
                if self.screen[i + 40*j] == 0:
                    print(".",end="")
                else:
                    print("#", end="")
            print("")



cpu = CPU()

for line in puzzlines:
    # print(line)
    # print(cpu.cycle)
    comm, num = parse_line(line)
    if comm == "addx ":
        cpu.inc_cyc()
        cpu.inc_cyc()
        cpu.addx(num)

    if comm == "noop":
        cpu.inc_cyc()

print("answer to day 10 part 1:")
print(cpu.sumsig)

print("Screen drawing:")
cpu.pretty_print()