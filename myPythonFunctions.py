from random import randint
from os import remove, rename

def getUserPoint(userName):
    try: 
        input = open ('userScores.txt', 'r')
        for line in input:
            content = line.split(',')
            if content[0] == userName:
                input.close()
                return content[1]
        input.close()
        return "-1"
    except IOError:
        print ("\nFile userScores.txt not found. A new file will be created.")
        input = open('userScores.txt', 'w')
        input.close()
        return "-1"

def updateUserPoints(newUser, userName, score):
    if newUser:
        input = open('userScores.txt', 'a')
        input.write('\n' + userName + ', ' + score)
        input.close()
    else:
        input = open('userScore.txt', 'r')
        output = open('userScores.tmp', 'w')
    for line in input:
        content = line.split(',')
        if content[0] == userName:
            content [1] = score
            line = content[0] + ', ' + content[1] + '\n'

            output.write(line)
        input.close()
        output.close()

        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
            
