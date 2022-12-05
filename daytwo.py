# day 2

puzzin = open("0201.txt", 'r')

puzzlines = puzzin.readlines()

def score(inputline):
    play, response = inputline
    # 1 for rock, 2 for paper, 3 for scissors
    playord = ord(play) - ord('A') + 1
    resord = ord(response) - ord('X') + 1
    if playord == resord:  # draw
        return 3 + resord
    elif (resord - playord) % 3 == 2: # loss
        return 0 + resord
    elif (resord - playord) % 3 == 1: # win
        return 6 + resord
    
def readinput(line):
    return (line[0], line[2])

scores = [score(readinput(line)) for line in puzzlines]

print(sum(scores))