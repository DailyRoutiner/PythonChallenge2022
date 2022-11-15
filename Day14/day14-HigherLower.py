import random
from art import logo, vs
import game_data

def randomData():
    return random.choices(game_data.data)[0]

def check_answer(user_answer, a_follower, b_follower):
    if (a_follower > b_follower ):
        return user_answer == 'A'
    else:
        return user_answer == 'B'
    
def game():
    score = 0
    is_game_over = False
    compareA = randomData()
    while is_game_over == False:
        compareB = randomData()
        while compareA == compareB: 
            compareB = randomData() 
        print(logo)
        print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}.")
        print(vs)
        print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}.")

        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        a_follower = compareA['follower_count'] 
        b_follower = compareB['follower_count']
        # Check Answer
        is_correct = check_answer(user_answer, a_follower, b_follower)

        # Clear display
        # clear()
         
        # Give feedback on their guess and score keeping
        if is_correct:
            score = score+1
            print(f"You're right! Current score: {score}.") 
            compareA = compareA if (user_answer == 'A') else compareB  # 삼항 연산자.
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_game_over = True

game()