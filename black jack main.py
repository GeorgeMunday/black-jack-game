import random
def game(bank):
    bet = 0
    card1 = 0
    card2 = 0
    card3 = 0
    total = 0
    win = 0
    status = ""
    exit = ""
    
    print(f"you have {bank} in your bank")
    bet =(input("how much would you like to bet"))
    if bet.isnumeric(): 
        bet = int(bet)
        while True:
            bank = bank - bet#how much you have left in your bank
            print(f"you have {bank} left in your bank")
            deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
            
             
            dealer_card1 = random.choice(deck)
            dealer_card2 = random.choice(deck)
            dealer_total = dealer_card1 + dealer_card2
            dealer_status = ""
            print(f"the dealer has {dealer_card1} and another card(use this information in your choice to hold or hit)")
                          
            card1= random.choice(deck)
            card2 = random.choice(deck)
            total = card1 + card2
            
            print(card1)
            print(card2)
            print(total)
            #ace handeling
            if total > 21:
                if card1 == 11 or card2 == 11:
                    total -= 10  # If the total is over 21, treat Ace as 1
                    print(f"Your total is now: {total}")
            
            else:
                while total < 21:
                    status = input("Do you want to 'hold' or 'hit': ").lower()
                    
                    if status == "hit":
                        card3 = random.choice(deck)
                        total += card3
                        print(f"You drew a {card3}, total is now {total}")
                        if total > 21:
                            print("You bust!")
                            break
                    elif status == "hold":
                        print(f"You hold with a total of {total}")
                        break
                    else:
                        print("Invalid choice! Please choose 'hold' or 'hit'.")
    
        # Dealer's turn
            if total <= 21:
                print(f"The dealer's cards: {dealer_card1} and {dealer_card2}, total: {dealer_total}")
                while dealer_total < 17:
                    dealer_card3 = random.choice(deck)
                    dealer_total += dealer_card3
                    print(f"Dealer drew a {dealer_card3}, dealer's total: {dealer_total}")
                
                if dealer_total > 21:
                    print("Dealer busts! You win!")
                    bank += bet * 2  # Player wins
                elif dealer_total > total:
                    print("Dealer wins!")
                elif dealer_total < total:
                    print(f"You win! Your total of {total} beats the dealer's total of {dealer_total}.")
                    bank += bet * 2
                else:
                    print("It's a tie!")
            
            # Ask for continuation
            exit_game = input("Do you want to play again? (yes/no): ").lower()
            if exit_game == "no":
                print("Exiting game...")
                break
            else:
                print(f"You now have £{bank} in your bank.")
                if bank <= 0:
                    print("You have no more money left. Exiting...")
                    break
    else:
        print("Invalid input for bet amount.")
    return bank
                
        

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