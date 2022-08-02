import random
def game_guess():   
    x = random.randrange(1, 1000)
    print(x)
    print("I have a guess between 1 and 1000.")
    print("can you guess my number?") 

    while True:
        n = int(input("please type your guess->"))
        if x == n:
            print("excellent! You guessed the number right!. would you like to try again?")
            a = input("y(yes) or n(no)?->")
            if a == "y" or a == "yes" or a == "YES" or a == "Yes" or a=="y(yes)":
                game_guess()
            break
        elif x > n:
            print("Too low. Try again")
        else:
            print("Too high. Try again")


game_guess()
