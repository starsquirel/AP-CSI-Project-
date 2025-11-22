import random
import time
import json
import os

# this is the wheel
wheel = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 23, 34, 15, 3, 24, 36, 13, 1, 00,
         27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]

# these are the lists to check what type the roll is
Black = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
Red   = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
Low   = list(range(1, 19))
High  = list(range(19, 37))
Even  = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
Odd   = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
Green = (0, 00)

Data = {
    "Chips": 0,
    "WINS": 0,
    "LOSSES": 0
}

Wait = 0.01
Chips = 0
Losses = 0
Wins = 0

# makes the text look like it is being typed out
def Text(words):
    global Wait
    for ch in words:
        if ch != ' ':
            time.sleep(Wait)
        print(ch, end='', flush=True)

# this function picks a random number in the wheel list
def roulettewheel():
    # chooses a random element in the wheel
    wheel_out = random.choice(wheel)
    return wheel_out

# this is the startup function
def StartUp():
    Text("Hello this is roulette\n\n")

    try:
        with open('save.json', 'r') as f:
            Data = json.load(f)
            Chips = Data["Chips"]
            Losses = Data["LOSSES"]
            Wins = Data["WINS"]
    except FileNotFoundError:
        Chips = 0
        Losses = 0
        Wins = 0

    if Chips == 0:
        Text("You have no chips\nYou should get some\n")
        main(Chips, Losses, Wins)

    main(Chips, Losses, Wins)

def ScreenClear():
    input("Press enter to continue\n")
    os.system('clear')

# this is the shutdown function
def Shutdown():
    Text("Goodbye\n")
    time.sleep(1)
    Text("Saving\n")
    Data["Chips"] = Chips
    Data["LOSSES"] = Losses
    Data["WINS"] = Wins
    with open('save.json', 'w') as f:
        json.dump(Data, f)
    Text("Shutting down\n")
    exit()

# main game loop
def main(Chips, Losses, Wins):
    while True:
        BLACKBG = '\033[100m'
        REDBG = '\033[41m'
        RESET = '\033[0m'

        # saves stats constantly
        Data["Chips"] = Chips
        Data["LOSSES"] = Losses
        Data["WINS"] = Wins
        with open('save.json', 'w') as f:
            json.dump(Data, f)

        Text("(1) to play, (2) to buy more chips, (3) Stats, (4) Exit\n")
        Choice1 = input("What do you want to do: ")

        if Choice1 == "1":
            os.system('clear')
            Text("(1) black, (2) red, (3) high, (4) low, (5) even, (6) odd, (7) green\n")
            Betting = input("\nWhat do you want to bet on: ")
            os.system('clear')

            if Betting == "1": Text("You are betting on black\n")
            elif Betting == "2": Text("You are betting on red\n")
            elif Betting == "3": Text("You are betting on high\n")
            elif Betting == "4": Text("You are betting on low\n")
            elif Betting == "5": Text("You are betting on even\n")
            elif Betting == "6": Text("You are betting on odd\n")
            elif Betting == "7": Text("You are betting on green\n")
            else:
                print("ERROR")

            Bet = int(input(f"You have {Chips} chips\nHow much do you want to bet (whole number): "))

            if Bet <= Chips and Bet > 1:
                roll = roulettewheel()

                if roll in Black:
                    print(BLACKBG + f"\n{roll} black\n" + RESET + "\n")
                if roll in Red:
                    print(REDBG + f"\n{roll} red" + RESET + "\n")

                # win/loss checks
                if Betting == "1":  # black
                    if roll in Black:
                        Text("You win\n")
                        Chips += Bet
                        Wins += 1
                        print(f"You now have: {Chips} chips\n")
                    else:
                        Chips -= Bet
                        Losses += 1
                        print(f"You lose! You now have: {Chips} chips\n")

                elif Betting == "2":  # red
                    if roll in Red:
                        Text("You win!\n")
                        Chips += Bet
                        Wins += 1
                        print(f"You now have: {Chips} chips\n")
                    else:
                        Chips -= Bet
                        Losses += 1
                        print(f"You lose! You now have: {Chips} chips\n")

                elif Betting == "3":  # high
                    if roll in High:
                        Text("You win!\n")
                        Chips += Bet
                        Wins += 1
                        print(f"You now have: {Chips} chips\n")
                    else:
                        Chips -= Bet
                        Losses += 1
                        print(f"You lose! You now have: {Chips} chips\n")

                elif Betting == "4":  # low
                    if roll in Low:
                        Text("You win!\n")
                        Chips += Bet
                        Wins += 1
                        print(f"You now have: {Chips} chips\n")
                    else:
                        Chips -= Bet
                        Losses += 1
                        print(f"You lose! You now have: {Chips} chips\n")

                elif Betting == "5":  # even
                    if roll in Even:
                        Text("You win!\n")
                        Chips += Bet
                        Wins += 1
                        print(f"You now have: {Chips} chips\n")
                    else:
                        Chips -= Bet
                        Losses += 1
                        print(f"You lose! You now have: {Chips} chips\n")

                elif Betting == "6":  # odd
                    if roll in Odd:
                        Text("You win!\n")
                        Chips += Bet
                        Wins += 1
                        print(f"You now have: {Chips} chips\n")
                    else:
                        Chips -= Bet
                        Losses += 1
                        print(f"You lose! You now have: {Chips} chips\n")

                elif Betting == "7":  # green
                    if roll in Green:
                        Chips += (Bet * 35)
                        Wins += 1
                        print(f"You win! You now have: {Chips} chips\n")
                    else:
                        Chips -= Bet
                        Losses += 1
                        print(f"You lose! You now have: {Chips} chips\n")

                ScreenClear()
            else:
                print("You don't have enough chips")

        elif Choice1 == "2":
            AddChips = int(input("\nHow much do you want to add: "))
            Chips += AddChips
            ScreenClear()

        elif Choice1 == "3":
            print(f"You have {Wins} wins and {Losses} losses\n\n")
            ScreenClear()

        elif Choice1 == "4":
            Shutdown()

        else:
            print("Invalid input")
            ScreenClear()

StartUp()
