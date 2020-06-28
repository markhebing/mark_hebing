z = "y"

while z == "y":

    print("Welcome to Rock Paper Scissors!")

    x = input("Player 1 make your choice: r = rock, p = paper, s = scissors ... ")
    y = input("Player 2 make your choice: r = rock, p = paper, s = scissors ... ")

    if x == "s" and y == "p":
        print("Scissors beats paper! Player 1 wins!")
    elif x == "p" and y == "r":
        print("Paper beats rock! Player 1 wins!")
    elif x == "r" and y == "s":
        print("Rock beats scissors! Player 1 wins!")
    elif y == "s" and x == "p":
        print("Scissors beats paper! Player 2 wins!")
    elif y == "p" and x == "r":
        print("Paper beats rock! Player 2 wins!")
    elif y == "r" and x == "s":
        print("Rock beats scissors! Player 2 wins!")
    elif x == y:
        print("Stalemate!!!")

    z = input("Would you like to start another game? (y/n) ... ")

if z == "n":
    print("Goodbye!")
