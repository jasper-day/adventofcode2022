# day 2

puzzin = open("0201.txt", 'r')

puzzlines = puzzin.readlines()

def score(inputline):
    play, response = inputline
    # 0 for rock, 1 for paper, 2 for scissors
    playord = ord(play) - ord('A')
    # 0 for lose, 1 for draw, 2 for win
    resord = ord(response) - ord('X')
    for testresponse in range(0,3):
        if (testresponse - playord)%3 == (resord - 1)%3:
            return testresponse + 1 + resord * 3

    
def readinput(line):
    return (line[0], line[2])

scores = [score(readinput(line)) for line in puzzlines]

print(sum(scores))