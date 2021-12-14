import random


def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
              "_______       ",
              "|      |      ",
              "|      |      ",
              "|      o      ",
              "|     /|\     ",
              "|     / \     "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman")

    while wrong < len(stages) - 1:
        print("\n")
        char = input("estimate 1 character : ")
        if char in rletters:
            cindex = rletters.index(char)
            board[cindex] = char
            rletters[cindex] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!\n")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The answer is {}".format(word))

hangman()    