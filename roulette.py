import random
def result_game():
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    number = random.choice ( list1)
    return number
def exit_game(bank):
    profit = bank - 100
    print(f"you profited £{profit}")
    exit()
    

def roulette (bank):
    choice1 = input("what would you like to bet on")



    result = result_game(bank)


def main():
    bank = 0
    play = ""
    
    # Welcome message
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
        
        
            
# Run the game
main()