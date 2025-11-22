import random
import time
import json
import os

#this is the weel
weel = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 23, 34, 15, 3, 24, 36, 13, 1, 00,27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]
#these are the lists to check what type the role is so I dont have make a lot more code
Black = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
Red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
Low = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
High = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
Even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
Odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
Green =(0, 00)
Data={
    "Chips": 0,
    "WINS": 0,
    "LOSSES": 0
    }

Wait = 0.01
Chips = int(0)
Losses = int(0)
Wins = int(0)
#makes the text look like it is being typed out
def Text(words):
    global Wait
    index = 0
    for i in range(len(words)):
        if words[index] != ' ':
            time.sleep(Wait)
            
        print(words[index], end='', flush=True)
        index += 1

#this function picks a random number in the weel list
def rouletteweel():
    # Chooses a random eliment in the weel
    weel_out = random.choice(weel)
    return weel_out

#this is the start up function
#when the game starts it loads the chips from the json file
def StartUp():
    Text("hello this is roulett\n\n")

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
        Text("you have no chips\n you should get some\n")
        main(Chips,Losses,Wins)
    main(Chips,Losses,Wins)
def ScreenClear():
    input("press enter to continue\n")
    os.system('clear')


#this is the shut down function
#when the game is shut down it saves the chips to the json file
#even though it saves every time the loop runs 
def Shutdown():
    Text("goodbye\n")
    time.sleep(1)
    Text("saving\n")
    Data["Chips"] = Chips
    Data["LOSSES"] = Losses
    Data["WINS"] = Wins
    with open('save.json', 'w') as f:
        json.dump(Data, f)
    Text("shutting down\n")
    exit()

#this is the main function where the game is played
def main(Chips,Losses,Wins):
    #makes a loop so the game can be played multiple times
    while True:
        BLACKBG = '\033[100m'#ansi color code
        REDBG = '\033[41m'
        RESET = '\033[0m'
        #saves the chips every time the loop runs
        Data["Chips"] = Chips
        Data["LOSSES"] = Losses
        Data["WINS"] = Wins
        with open('save.json', 'w') as f:
            json.dump(Data, f)

        #This is the main menu
        Text("(1)to play,(2)to buy more chips,(3)Stats,(4) exit\n")
        Choice1 = input("what do you want to do: ")
        if Choice1 == "1":
            os.system('clear')
            Text("(1)black,(2)red,(3)high,(4)low, (5)even, (6)odd, (7)green\n")
            #this is where the user chooses what they want to bet on
            Betting = input("\nwhat do you want to bet on: ")
            os.system('clear')
            if Betting == "1":
                Text("you are betting on black\n")
            elif Betting == "2":
                Text("you are betting on red\n")
            elif Betting == "3":
                Text("you are betting on high\n")
            elif Betting == "4":
                Text("you are betting on low\n")
            elif Betting == "5":
                Text("you are betting on even\n")
            elif Betting == "6":
                Text("you are betting on odd\n")
            elif Betting == "7":
                Text("you are betting on green\n")
            else:
                print("ERROR")
            #this is where the user bets their chips
            Bet = int(input(f"you have {Chips} chips\nhow much do you want to bet(whole num): "))
            #this just checks if the user has enough chips to bet
            if Bet <= Chips and Bet > 1:
                role = rouletteweel()
                #this prints the role and prints if it is black or red
                if role in Black:
                    print(BLACKBG+f"\n{role} black\n"+RESET+"\n")
                if role in Red:
                    print(REDBG+f"\n{role} red"+RESET+"\n")

                #this checks if the user won or lost
                #and does math to + or - chips
                if Betting == "1":
                    if role in Black:
                        Text("you win\n")
                        Chips = Chips + Bet
                        Wins = Wins + 1
                        print(f"you now have:{Chips} chips\n")
                    else:
                        Chips = Chips - Bet
                        Losses = Losses + 1
                        print(f"you Loose! you now have:{Chips} chips\n")
                elif Betting == "2":
                    if role in Red:
                        Chips = Chips + Bet
                        Wins = Wins + 1
                        print(f"you win! you now have:{Chips} chips\n")
                    else:
                        Chips = Chips - Bet
                        Losses = Losses + 1
                        print(f"you Loose! you now have:{Chips} chips\n")
                elif Betting == "3":
                    if role in High:
                        Chips = Chips + Bet
                        Wins = Wins + 1
                        print(f"you win! you now have:{Chips} chips\n")
                    else:
                        Chips = Chips - Bet
                        Losses = Losses + 1
                        print(f"you Loose! you now have:{Chips} chips\n")
                elif Betting == "4":
                    if role in Low:
                        Chips = Chips + Bet
                        Wins = Wins + 1
                        print(f"you win! you now have:{Chips} chips\n")
                    else:
                        Chips = Chips - Bet
                        Losses = Losses + 1
                        print(f"you Loose! you now have:{Chips} chips\n")

                elif Betting == "5":
                    if role in Even:
                        Chips = Chips + Bet
                        Wins = Wins + 1
                        print(f"you win! you now have:{Chips} chips\n")
                    else:
                        Chips = Chips - Bet
                        Losses = Losses + 1
                        print(f"you Loose! you now have:{Chips} chips\n")
                elif Betting == "6":
                    if role in Odd:
                        Chips = Chips + Bet
                        Wins = Wins + 1
                        print(f"you win! you now have:{Chips} chips\n")
                    else:
                        Chips = Chips - Bet
                        Losses = Losses + 1
                        print(f"you Loose! you now have:{Chips} chips\n")
                elif Betting == "7":
                    if role in Green:
                        Chips = (Bet * 35) + Chips
                        Wins = Wins + 1
                        print(f"you win! you now have:{Chips} chips\n")
                    else:
                        Chips = Chips - Bet
                        Losses = Losses + 1
                        print(f"you Loose! you now have:{Chips} chips\n")
                        
                else:
                    print("ERROR")
                
                ScreenClear()
            else:
                print("you dont have enough chips")
        
        #This just adds chips
        elif Choice1 == "2":
            AddChips = int(input("\nhow much do you want to add: "))
            Chips = Chips + AddChips
            ScreenClear()
        
        elif Choice1 == "3":
            print(f"you have {Wins} wins and {Losses} losses\n\n")
            ScreenClear()

        
        #as the function says it shuts done
        elif Choice1 == "4":
            Shutdown()

        
        else:
            print("invalid input")
            ScreenClear()


StartUp()
