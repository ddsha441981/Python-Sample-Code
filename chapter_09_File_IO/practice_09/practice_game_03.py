# Author: Deendayal Kumawat
""" Date: 02/03/20
Descriptions: File & IO"""


def game():
    return 44677


score = game()
with open("highscore.txt") as f:
    hiScoreStr = f.read()

if hiScoreStr == '':
    with open("highscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr) < score:
    with open("hiscore.txt", "w") as f:
        f.write(str(score))