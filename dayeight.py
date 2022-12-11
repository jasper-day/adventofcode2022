import itertools
import re
import os
import sys
import random
import numpy as np


puzzin = open("0801.txt", "r")
puzzlines = puzzin.readlines()

def treesfromleft(line):
    maxheight = 0
    count = 0
    for tree in line:
        tree = int(tree)
        if tree > maxheight:
            maxheight = tree
            print(tree)
            count += 1
    return count

def treesfromright(line):
    maxheight = 0
    count = 0
    for i in np.arange(len(line)-1, 0, -1):
        tree = int(line[i])
        if tree > maxheight:
            maxheight = tree
            count += 1
    return count

count = 0
class Puzzarray():
    def __init__(self):
        self.array = []
        self.nparray = np.array([])
    def tallest_tree(self,i,j):
        def max_row(i,j):
            try:
                return min(self.nparray.take(i,0)[:j].max(), self.nparray.take(i,0)[j+1:].max())
            except:
                print(f"exception occurred at {i}, {j}")
                return 0
        def max_column(i,j):
            try:
                return min(self.nparray.take(j,1)[:i].max(), self.nparray.take(j,1)[i+1:].max())
            except:
                print(f"exception occurred at {i}, {j}")
                return 0
        
        if self.nparray[i,j] > min(max_row(i,j), max_column(i,j)):
            print(f"tree found at {i}, {j}")
            print(f"Max row: {max_row(i, j)}, max column: {max_column(i, j)}")
            return True
    def scenic_score(self, i,j):
        value = self.nparray[i,j]
        row = self.nparray.take(i,0)
        column = self.nparray.take(j,1)
        up, down, left, right = 1,2,1,2
        hup, hdown, hleft, hright = 0,0,0,0
        while j-left > 0 and row[j-left] >= max(row[j-left:j]):
            left += 1
            if max(row[j-left:j]) < value: 
                break
        left -= 1
        while max(row[j+1:j+right]) < value and row[j+right-1] >= max(row[j+1:j+right]) and j+right < len(row):
            right += 1
        right -= 1
        while max(column[j-up:j]) < value and column[j-up] >= max(column[j-up:j]) and j-up > 0:
            up += 1
        up -= 1
        while max(column[j+1:j+down]) < value and column[j+down-1] >= max(column[j+1:j+down]) and j+down < len(column):
            down += 1
        down -= 1
        score = up*down*left*right
        print(f"row: {i}, col: {j}, left: {left}, right: {right}, up:{up}, down:{down}, score:{score}")
        # awful awful awful

    def scenic_score_improved(self,i,j):
        value = self.nparray[i,j]
        row = self.nparray.take(i,0)
        column = self.nparray.take(j,1)
        up, down, left, right = 1,1,1,1
        hup, hdown, hleft, hright = 0,0,0,0

        while True:
            if row[j - left] == -1:
                left -= 1
                break
            if row[j - left] >= hleft:
                hleft = row[j - left]
            # if row[j - left] < hleft:
            #     left -= 1
            #     break
            if hleft >= value:
                break
            left += 1

        while True:
            if column[i - up] == -1:
                up -= 1
                break
            if column[i - up] >= hup:
                hup = column[i - up]
            # if column[i - up] < hup:
            #     up -= 1
            #     break
            if hup >= value:
                break
            up += 1

        while True:
            if row[j + right] == -1:
                right -= 1
                break
            if row[j + right] >= hright:
                hright = row[j + right]
            # if row[j + right] < hright:
            #     right -= 1
            #     break
            if hright >= value:
                break
            right += 1

        while True:
            if column[i + down] == -1:
                down -= 1
                break
            if column[i + down] >= hdown:
                hdown = column[i + down]
            # if column[i + down] < hdown:
            #     down -= 1
            #     break
            if hdown >= value:
                # print(f"broke at down = {down}", end="")
                break
            down += 1

        score = up*down*left*right
        if (i == 2 and j == 3) or ( i == 4 and j == 3):
            print(f"row: {i}, col: {j}, left: {left}, right: {right}, up:{up}, down:{down}, score:{score}")
        return score
        
parr = Puzzarray()

for line in puzzlines:
    line = line.strip()
    # count += treesfromleft(line)
    # count += treesfromright(line)
    parr.array.append([int(i) for i in line])

parr.nparray = np.array(parr.array)
parr.nparray = np.pad(parr.nparray,1,'constant',constant_values=-1)
print(parr.nparray)
# np.transpose(puzzarray)

scores = []

for i in range(1,len(parr.array[0])+1):
    for j in range(1,len(parr.array)+1):
        scores.append(parr.scenic_score_improved(i,j))


print("Answer to day 8 part 2:")
print(max(scores))

