import random
def game(bank):
    bet =(input("how much would you like to bet"))
    
    if bet.isnumeric(): 
        bet = int(bet)
        while True:
            bank = bank - bet#how much you have left in your bank
            print(f" you have {bank} in your bank")
            deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
            break
    else:
        print("invalid input")
        

def main():
    print("Welcome to Balck Jack")  #introduction
    play =  input("are you over the age of 18 (yes/no)").lower() #.lower so the input is lower case so doesnt mess up if statment

    if play == "yes":
        play = True#activating the while loop
    elif play == "no":
        print("you are not the lega; age to play this game")
    else:
        play = False
        print("invalid input")
        
    while play == True:
        bank = input("how much money do you want to put in your bank")
        bank_int = bank.isnumeric()#validation that it is a number so the code doesnt break
        
        if bank_int == True:
            print(f"you put in £{bank}")
            break
        else:
            print("please enter a valid input")

        game(bank)

main()