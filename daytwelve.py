import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib as mpt

mpt.style.use("dark_background")
# plt.ion()

puzzin = open("1201.txt")
puzzlines = puzzin.readlines()

PRINT_FLAG = False

def parse_line(line):
    line.strip()
    linere = re.compile(r"(S|E|.)")
    mo = linere.findall(line)
    start, end = None, None
    heights = []
    for index in range(len(mo)):
        if mo[index] == "S":
            start = index
            heights.append(0)
        elif mo[index] == "E":
            end=index
            heights.append(26)
        else: heights.append(ord(mo[index]) - ord('a'))
    return heights, start, end

    

class Hill():
    def __init__(self, heights, start, end, ax, fig):
        self.hax = ax
        # self.dax = ax[1]
        self.heights = heights
        self.distances = np.zeros(self.heights.shape)
        self.visited = np.zeros(self.heights.shape)
        self.start = start
        self.end = end
        self.right = np.array([1,0])
        self.up = np.array([0,1])
        # self.dax.imshow(self.distances)
        self.fig = fig
    def dijkstra(self, bug, distance):
        # plt.pause(0.01)
        if PRINT_FLAG:
            print(f"testing location at {bug}")
            print(f"cell value: {self.distances[self.loc(bug)]}, current distance: {distance}")
        if self.distances[self.loc(bug)] > distance or self.distances[self.loc(bug)] == 0:
            # self.dax.imshow(self.distances)
            # self.fig.canvas.draw()
            # self.fig.canvas.flush_events()
            self.distances[self.loc(bug)] = distance
            vsquares = self.valid_squares(bug)
            for vsquare in vsquares:
                self.dijkstra(vsquare, distance + 1)

    def valid_squares(self, bug):
        value = self.heights[self.loc(bug)]
        def test_square(location):
            try:
                return self.heights[self.loc(location)] >= value - 1
            except:
                return False
        squares = []
        for location in [bug + self.right, bug - self.right, bug + self.up, bug - self.up]:
            if test_square(location):
                squares.append(location)
        return squares
    
    def loc(self, array):
        return array[0], array[1]



fig = plt.figure()
ax = plt.axes(projection="3d")


heights = []
for i in range(len(puzzlines)):
    height, start, end = parse_line(puzzlines[i])
    if start != None:
        starc = np.array([i,start])
    if end != None:
        endc = np.array([i, end])
    heights.append(height)

heights = np.array(heights)

hill = Hill(heights, starc, endc, ax, fig)
print(hill.heights)
hill.dijkstra(hill.end, 0)
print(hill.distances)
print("Answer to day 12:")
print(hill.distances[hill.loc(hill.start)])

print("Answer to day 12 part 2:")
signs = np.sign(hill.heights)
alocs = np.ones(hill.heights.shape) - signs
adistances = alocs * hill.distances
alist = adistances.flatten().tolist()
while 0 in alist:
    alist.remove(0)
print(min(alist))

# ax[1].imshow(hill.distances)
x = np.arange(hill.heights.shape[1])
y = np.arange(hill.heights.shape[0])
X, Y = np.meshgrid(x,y)
hill.hax.plot_surface(X,Y,hill.heights,cmap="viridis")

plt.show()