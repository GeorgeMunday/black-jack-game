import random
import time
def result_game():
    list1 = [random.randint(0,36)]
    number = random.choice ( list1)
    return number

def exit_game(bank):
    profit = bank - 100
    print(f"you profited £{profit}")
    exit()
    


def roulette (bank):
    print(f"\n You have £{bank} left in your bank.\n")
    bet =input("How much would you like to bet? £")
    if bet == "0":
        exit_game()                      
    else:
        if bet.isnumeric(): 
            bet = int(bet)
            bank = bank - bet
            choice1 = ""
            choice2 = ""
            result = result_game()
            condition = ""
            status = ""
            choice1 = input("what would you like to bet on:\n 1. colour,2. odd or even ,3. number\n ")
            while choice1 == "1":
                print(f"you have {bank} in your bank ")
                choice2 = input("would you like to bet on red or black")
                print("spinning...")
                time.sleep(1)
                print("spinning...")
                time.sleep(1)
                print("spinning...")
                print(f"it landed on {result}")
                if result % 2 == 0:
                    condition = "red"
                    print(f"it is {condition}")
                if result % 2 != 0:
                    condition = "black"
                    print(f"it is {condition}")
                if condition == choice2:
                    status = "win"
                    print("you win")
                    
                else:
                    status = "lose"
                    print("you lose")
                    
                    
                
                if status == "win":
                    bet = bet * 2
                    bank += bet
                else:
                    bank = bank
                    
            while choice1 == "2":
                print(f"you have {bank} in your bank ")
                choice2 = input("would you like to bet on odd or even")
                print("spinning...")
                time.sleep(1)
                print("spinning...")
                time.sleep(1)
                print("spinning...")
                print(f"it landed on {result}")
                if result % 2 == 0:
                    condition = "even"
                    print(f"it is {condition}")
                if result % 2 != 0:
                    condition = "odd"
                    print(f"it is {condition}")
                if condition == choice2:
                    status = "win"
                    print("you win")
                else:
                    status = "win"
                    print("you lose")
                
                if status == "win":
                    bet = bet * 2
                    bank += bet
                else:
                    bank = bank       
            while choice1 == "3":
                print(f"you have {bank} in your bank ")
                choice2 = input("what number do you want to bet on")
                int(choice2)
                print("spinning...")
                time.sleep(1)
                print("spinning...")
                time.sleep(1)
                print("spinning...")
                print(f"it landed on {result}")
                if condition == choice2:
                    print("you win")
                    status = "win"
                    break
                else:
                    status = "lose"
                    print("you lose")
                    
                if status == "win":
                    bet = bet * 36
                    bank += bet
                else:
                    bank = bank
                    
        else:
            print("invalid input")
            roulette(bank)
            
        

def main():
    bank = 0
    play = ""
    
    
    print("\n Welcome to roulette! ")
    print(" Try your luck and win big! ")
    print("-" * 40)
    
    play = input("Are you over the age of 18? (yes/no): ").lower()
    if play == "yes":
        play = True
    elif play == "no":
        print("\n You are not of legal age to play this game.")
        return
    else:
        print("\nInvalid input. Please restart the game.")
        return
    
    while play == True :
        bank = 100
        print(f"you have this much in your bank{bank}")
        roulette(bank)
        break





       
main()