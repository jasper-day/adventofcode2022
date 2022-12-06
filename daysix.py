
puzzin = open("0601.txt")
puzzstr = puzzin.read()


def find_index(puzzstr):
    count = 0
    last4 = []
    for letter in puzzstr:
        count += 1
        last4.append(letter)
        print(last4)
        if len(last4) > 14: # 4 for part 1, 14 for part 2
            last4.pop(0)
            if all_different(last4):
                return count
        
def all_different(string):
    for index in range(0,len(string)):
        letter = string[index]
        iterators = [*range(0,len(string))]
        iterators.remove(index)
        newstr = [string[iterator] for iterator in iterators]
        if letter in newstr:
            return False
    return True

print("Answer to day 6:")
print(find_index(puzzstr))
