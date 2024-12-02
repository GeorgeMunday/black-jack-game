import random
def main(bank):
    bet = int(input("how much would you like to bet"))
    bank = bank - bet
    print(bank)
    your_card1 = random.randint(1,11)
    your_card2 = random.randint(1,11)
    dealer_hand = random.randint(1,11)
    dealer_hand = random.randint(1,11)
    
    
    



print("Welcome to Balck Jack")  #introduction
play =  input("are you over the age of 18 (yes/no)").lower() #.lower so the input is lower case so doesnt mess up if statment

if play == "yes":
    play = True#activating the while loop
else:
    play = False
    print("you are not above the legal age to play this game")
    
while play == True:
    bank = input("how much money do you want to put in your bank")
    bank_int = bank.isnumeric()#validation that it is a number so the code doesnt break
    
    if bank_int == True:
        print(f"you put in £{bank}")
        break
    else:
        print("please enter a valid input")
print("here are the rules;\n1.your goal is to get the closes you can to 21\n2.the dealer will be doing the same if they beat you you lose")
print("if you win")
main(bank)