import random
import time
#these are the lists to check what type the role is
Black = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
Red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
Low = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
High = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
Even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
Odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
weel = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 23, 34, 15, 3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]


Chips = 100
Wait = 0.05
def Text(words):
    global Wait
    index = 0
    for i in range(len(words)):
        if words[index] != ' ':
            time.sleep(Wait)

        print(words[index], end='', flush=True)
        index += 1

       
Text("hello this is roulet\n")

def rouletteweel():
# Chooses a random eliment in the weel
    weel_out = random.choice(weel)
    return weel_out
def main(Chips):
    while True:
        
        print("(1)to play,(2)to buy more chips,(3) exit\n")
        Choice1 = input("what do you want to do: ")
        if Choice1 == "1":
            Text ("(1)black,(2)red,(3)high,(4)low, (5)even, (6)odd\n")
            Choice2 = input("what do you want to bet on: ")
            print(Chips)
            Bet = int(input("how much do you want to bet(whole num): "))
            if Bet <= Chips and Bet > 0:
                role = rouletteweel() 
                print(f"You roled \n--{role}--\n")
                if Choice2 == "1":
                    if role in Black:
                        Text("you win\n")
                        Chips = Chips + Bet
                        print(f"you win! you now have:{Chips} chips\n") 
                    else: 
                        Chips = Chips - Bet
                        print(f"you Loose! you now have:{Chips} chips\n")
                elif Choice2 == "2":
                    if role in Red:
                        Text("you win\n")
                        Chips = Chips + Bet
                        print(f"you win! you now have:{Chips} chips\n") 
                    else: 
                        Chips = Chips - Bet
                        print(f"you Loose! you now have:{Chips} chips\n")
                elif Choice2 == "3":
                    if role in High:
                        Text("you win\n")
                        Chips = Chips + Bet
                        print(f"you win! you now have:{Chips} chips\n") 
                    else: 
                        Chips = Chips - Bet
                        print(f"you Loose! you now have:{Chips} chips\n")
                elif Choice2 == "4":
                    if role in Low:
                        Text("you win\n")
                        Chips = Chips + Bet
                        print(f"you win! you now have:{Chips} chips\n") 
               
