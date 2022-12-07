import itertools
import re
import os
import sys
import random
import anytree
import treelib

puzzin = open("0701.txt", "r")
puzzlines = puzzin.readlines()

class Graph():
    def __init__(self):
        self.nodes = {}
    def add_node(self, name):
        self.nodes[name] = []
    def add_file(self, size, name, extension, node):
        self.nodes[node].append({"name":name, "ext": extension, "size":size})


MAXSIZE = 100000

def parse_line(line):
    regcd = re.compile(r"\$ cd (.*)")
    mocd = regcd.match(line)
    if mocd: # command
        return "cd", mocd.group(1)

    regls = re.compile(r"\$ ls")
    mols = regls.match(line)
    if mols: # command
        return "ls", "empty"

    regdir = re.compile(r"dir (.+)")
    modir = regdir.match(line)
    if modir:
        return "dir", modir.group(1)

    regfile = re.compile(r"(\d+) (\w+)\.?(\w+)?")
    mofile = regfile.match(line)
    if mofile:
        if mofile.group(3):
            return "file", [int(mofile.group(1)), mofile.group(2), mofile.group(3)]
        else:
            return "file", [int(mofile.group(1)), mofile.group(2), ""]


# filegraph = Graph()


class File():
    def __init__(self, size, name, ext):
        self.name = name
        self.ext = ext
        self.size = size

filetree = treelib.Tree()
identifier = 0
filetree.create_node("Root","root")
curr_dir = filetree.get_node("root")

for line in puzzlines:
    identifier += 1
    line = line.strip()
    command, result = parse_line(line)
    if command == "cd":
        if result == "..":
            curr_dir = filetree.get_node(filetree.parent(curr_dir.identifier).identifier)
        else: 
            for child in filetree.children(curr_dir.identifier):
                if child.tag == result:
                    curr_dir = child
    if command == "ls":
        pass
    if command == "dir":
        filetree.create_node(tag=result, identifier=identifier, parent = curr_dir.identifier)
    if command == "file":
        filetree.create_node(tag=(result[1] + "." + result[2]), identifier=identifier,data = File(size=int(result[0]), name=result[1], ext=result[2]), parent = curr_dir.identifier)

def get_size(node):
    total = 0
    for nodeid in filetree.expand_tree(node.identifier):
        if nodeid != node.identifier and filetree.get_node(nodeid).data:
            # print(f"node: {filetree.get_node(nodeid).tag}, size={filetree.get_node(nodeid).data.size}")
            total += filetree.get_node(nodeid).data.size
    return total

total = 0

for node in filetree.expand_tree():
    size = get_size(filetree.get_node(node))
    if size < MAXSIZE:
        total += size

print("Answer to day 7:")
print(total)

print("Answer to day 7 part 2:")

TOTAL = 70000000
NEEDED = 30000000

curr_use = get_size(filetree.get_node("root"))

HAVE = TOTAL - curr_use
WANT = NEEDED - HAVE

good_enough = []

for node in filetree.expand_tree():
    size = get_size(filetree.get_node(node))
    if size > WANT:
        good_enough.append(size)

print(min(good_enough))

    