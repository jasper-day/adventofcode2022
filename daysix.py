
puzzin = open("0601.txt")
puzzstr = puzzin.read()


def find_index(puzzstr, number):
    count = 0
    laststr = []
    for letter in puzzstr:
        count += 1
        laststr.append(letter)
        if len(laststr) > number: # 4 for part 1, 14 for part 2
            laststr.pop(0)
            if all_different(laststr):
                return count
# Horrible and inefficient
def all_different(string):
    for index in range(0,len(string)):
        letter = string[index]
        iterators = [*range(0,len(string))]
        iterators.remove(index)
        newstr = [string[iterator] for iterator in iterators]
        if letter in newstr:
            return False
    return True

print("Answer to day 6 part 1:")
print(find_index(puzzstr, 4))
print("Answer to day 6 part 2:")
print(find_index(puzzstr, 14))
