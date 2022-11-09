############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
starter = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

def resultGame(myCard, comCard):
    myCardSum = sum(myCard)
    computeSum = sum(comCard)
    print(f"Your final hand: {myCard}, final score: {myCardSum}")
    print(f"Computer's final hand: {comCard}, final score: {computeSum}")

def calculate_score(myCard, comCard):
    # add up user and computer cards
    myCardSum = sum(myCard)
    computeSum = sum(comCard)
        
    # Show myCard 
    print(f"Your cards: {myCard}, current score: {myCardSum}")
    print(f"Computer's first card: {comCard[0]}")
    # have ace?
    if myCardSum > 21 and 11 in myCard:
        myCard.remove(11)
        myCard.append(1)
        myCardSum = sum(myCard)
        if myCardSum > 21:
            resultGame(myCard, comCard)
            print("You went over. You lose 😭")
        
    elif computeSum == 21:
        resultGame(myCard, comCard)
        print("You lose Computer with a Blackjack 😭")   
    elif myCardSum == 21:
        resultGame(myCard, comCard)
        print("Win with a Blackjack 😎")
    elif computeSum > 21:
        resultGame(myCard, comCard)
        print("Computer went over. You Win 😎")


    # Add Card
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while another_card == "y":
        myCard.append(random.choice(cards))
        if computeSum < 17:
            comCard.append(random.choice(cards))
        myCardSum = sum(myCard)
        computeSum = sum(comCard)
        calculate_score(myCard, comCard)
    
    if myCardSum > computeSum:
        resultGame(myCard, comCard)
        print("You win 😎")
    elif myCardSum == computeSum:
        resultGame(myCard, comCard)
        print("Draw 😭")
    else:
        resultGame(myCard, comCard)
        print("You lose 😭")

while starter=="y":
    myCard =[] 
    comCard = []
    myCardSum =0 
    computeSum = 0
    # 2 times add cards
    for _ in range(2):
        myCard.append(random.choice(cards))
        comCard.append(random.choice(cards))
    
    # Calculate Blackjack
    calculate_score(myCard, comCard)

    starter = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()


