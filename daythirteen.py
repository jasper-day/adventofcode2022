# Solution for Day 13 
import numpy as np
import copy

PRINT_FLAG = False

puzzin = open("1301.txt")
puzzlines = puzzin.readlines()

def parse_list(line):
    out_list = eval(line)
    return out_list

def compare_lists(list1, list2):
    lenlist2 = len(list2)
    lenlist1 = len(list1)
    if min([lenlist2, lenlist1]) == 0:
        if lenlist2 > 0:
            if PRINT_FLAG:
                print("Left list ran out of items first!")
            return True
        elif lenlist1 > 0:
            if PRINT_FLAG:
                print("Right list ran out of items first!")
            return False
        else:
            if PRINT_FLAG:
                print("Lists were equivalent")
            return None
    else:
        left = list1.pop(0)
        right = list2.pop(0)

    if PRINT_FLAG:
        print(f"Comparing: {left} and {right}")

    if type(left) == int and type(right) == int:
        if left > right:
            if PRINT_FLAG:
                print("Failed by integer test")
            return False
        elif left < right:
            if PRINT_FLAG:
                print("Passed by integer test")
            return True
        else:
            return compare_lists(list1,list2)
    elif type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]
    # now we have two lists, left and right.
    res = compare_lists(left, right)
    if res == True or res == False:
        return res
    if res == None:
        return compare_lists(list1, list2)

def part_1_solution():
    sumindex = 0

    for i in range(0,len(puzzlines)//3+1):
        fval = parse_list(puzzlines[i*3])
        sval = parse_list(puzzlines[i*3 + 1])
        if PRINT_FLAG:
            print(f"Pair {i +1}: comparing {fval} and {sval}")
        res = compare_lists(fval, sval)
        if PRINT_FLAG:
            print(res)
        if res:
            sumindex += i + 1
        
    print("Answer to day 13 part 1:")
    print(sumindex)

def part_2_solution():
    parsed_lines = [parse_list(line) for line in filter(lambda n: len(n) > 1, puzzlines)]
    div1 = [[2]]
    div2 = [[6]]
    parsed_lines.append(div1)
    parsed_lines.append(div2)
    print("\n".join([str(i) for i in parsed_lines]))
    def swap_lines(index):
        parsed_lines[index], parsed_lines[index + 1] = parsed_lines[index + 1], parsed_lines[index]
    ops = 1
    sort_iterations = 0
    highest_index = 0
    while ops > 0:
        sort_iterations += 1
        ops = 0
        swap_index = 0
        for index in range(len(parsed_lines)-1):
            l1 = copy.deepcopy(parsed_lines[index])
            l2 = copy.deepcopy(parsed_lines[index + 1])
            res = compare_lists(l1,l2)
            if not res:
                swap_lines(index)
                swap_index = index
                if highest_index < swap_index:
                    highest_index = swap_index
                ops += 1
                break
        print(f"iteration {sort_iterations}, index swap: {swap_index}, highest index: {highest_index}")
        # print("\n".join([str(line) for line in parsed_lines]))

    i1 = parsed_lines.index(div1)+1
    i2 = parsed_lines.index(div2)+1
    print("Answer to day 13 part 2:")
    print(i1 * i2)

    
if __name__ == "__main__":
    part_2_solution()