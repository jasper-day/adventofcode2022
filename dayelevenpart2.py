import re 
import numpy as np

PRINT_FLAG = False

puzzin = open("1101.txt")
puzzlines = puzzin.readlines()

class Monkey():
    def __init__(self, number, items, operation, test, true, false):
        self.number = int(number)
        self.items = self.string_to_list(items)
        self.testnum = int(test)
        self.operation = self.string_to_ope(operation)
        self.test = lambda val: val%int(test) == 0
        self.true = int(true)
        self.false = int(false)
    
    def print_attrs(self):
        print(f"Monkey number: {self.number}")
        print(f"Monkey items: {self.items}")
        print(f"Monkey operation applied to 1: {self.operation(1)}")
        print(f"Monkey modulus: {self.test}")
        print(f"Monkey true: {self.true}")
        print(f"Monkey false: {self.false}")

    def string_to_list(self, inp_string):
        numsre = re.compile(r"\d+")
        mo = numsre.findall(inp_string)
        return [int(res) for res in mo]

    def string_to_ope(self, inp_string):
        return lambda old:eval(inp_string)

    def inspect_item(self, item):
        if PRINT_FLAG:
            print(f"Monkey {self.number} inspects item with a worry level of {item}")
        newval = self.operation(item)
        if PRINT_FLAG:
            print(f"Worry level is now {newval}")
        # newval = int(np.sqrt(newval)//1)
        if self.test(newval):
            return self.true, newval
        else:
            return self.false, newval

def make_monkey(lines):
    monkeyre = re.compile(r"Monkey (\d+)")
    itemsre = re.compile(r"Starting items: ((\d+).*)")
    opere = re.compile(r"Operation: new = (.*)")
    testre = re.compile(r"Test: divisible by (\d+)")
    truere = re.compile(r"If true: throw to monkey (\d+)")
    falsere = re.compile(r"If false: throw to monkey (\d+)")
    regexes = [monkeyre, itemsre, opere, testre, truere, falsere]
    results = {"number": "", "items": "", "operation": "", "test": "", "true": "", "false": ""}
    for line in lines:
        line = line.strip()
        for reg in regexes:
            mo = reg.search(line)
            if mo:
                res = mo.group(1)
                if reg == monkeyre:
                    results["number"] = res
                elif reg == itemsre:
                    results["items"] = res
                elif reg == opere:
                    results["operation"] = res
                elif reg == testre:
                    results["test"] = res
                elif reg == truere:
                    results["true"] = res
                elif reg == falsere:
                    results["false"] = res
    return Monkey(**results)

monkeys = []

for i in range((len(puzzlines) +1) // 7):
    monkey = make_monkey(puzzlines[7*i:7+7*i])
    monkeys.append(monkey)
    if PRINT_FLAG:
        monkey.print_attrs()
        print("")
        
inspections = [0 for i in range(len(monkeys))]


gcd = 1
for monkey in monkeys:
    gcd *= monkey.testnum

def oneround(monkeys):
    global i
    for monkey in range(len(monkeys)):
        if PRINT_FLAG:
            print(f"Monkey: {monkey}, items: {monkeys[monkey].items}")
        for item in monkeys[monkey].items:
            target, newval = monkeys[monkey].inspect_item(item)
            if PRINT_FLAG:
                print(f"Monkey: {monkey}, round: {i}, item:{item} target: {target}")
            newval %= gcd
            throw(monkeys, monkey, target, newval)
            inspections[monkey] += 1
        monkeys[monkey].items = []

def throw(monkeys,thrower,target, newval):
    if PRINT_FLAG:
        print(f"item with worry level {newval} is thrown to monkey {target}")
    monkeys[target].items.append(newval)

def total_items(monkeys):
    total = 0
    for monkey in monkeys:
        total += len(monkey.items)
    return total

for i in range(10000):
    # print(f"Number of items:{total_items(monkeys)}")
    oneround(monkeys)

print("Answer to day 11 part 1:")

maxim = max(inspections)
inspections.remove(maxim)
print(maxim * max(inspections))