import random
def game(bank):
    bet = 0
    card1 = 0
    card2 = 0
    card3 = 0
    total = 0
    bet =(input("how much would you like to bet"))
    status = ""
    
    if bet.isnumeric(): 
        bet = int(bet)
        while True:
            bank = bank - bet#how much you have left in your bank
            print(f"you have {bank} in your bank")
            deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
            
            card1= random.choice(deck)
            card2 = random.choice(deck)
            total = card1 + card2
            
            print(card1)
            print(card2)
            print(total)
            
            if card1 == 11 and card2 == 11:
                total = 2
                print(total)
            elif card1 == 11:
                number1=int(input("do you want an 11 or a 1"))
                if number1 == 11:
                    total = 11 + card2
                    print(total)
                else:
                    total = 1 + card2
            elif card2 == 11:
                number2=int(input("do you want an 11 or a 1"))
                if number2 == 11:
                    total = 11 + card1
                    print(total)
                else:
                    total = 1 + card1
            
            else:
                total = 1 +card1
            status = input("do you want to hold or hit")
            break
        while status == "hit" and status != "hold" and status != "bust":
            card3 = random.choice(deck)
            total = card1 + card2 + card3
            print(total)
            if total > 21:
                status = "bust"
                print("you bust")
                break
            elif total < 21 :
                status = input("do you want to hold or hit")
                if status == "hit":
                    continue
                elif status == "hold":
                    break
                
    else:
        print("invalid input")
        

def main():
    bank = 0
    play = ""
     
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
        bank = int(bank)
        if bank_int == True:
            print(f"you put in £{bank}")
            game(bank)
            break
        else:
            print("please enter a valid input")


main()