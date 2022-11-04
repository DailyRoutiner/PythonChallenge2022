import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
competitor = random.randint(0,2)
set = [rock, paper, scissors]

if player < competitor:
    if player==0 and competitor == 2:
        print(f"Competitor \n {set[competitor]}")
        print(f"You \n {set[player]} You Win!")    
    else:
        print(f"Competitor \n {set[competitor]}")
        print(f"You \n {set[player]} You Lose!")
elif player == competitor:
    print(f"Competitor \n {set[competitor]}")
    print(f"You \n {set[player]} It's draw!")
else:
    if player==2 and competitor == 0:
        print(f"Competitor \n {set[competitor]}")
        print(f"You \n {set[player]} You Lose!") 
    elif player >=3:
        print(f"Invalid number, You Lose!")
    else:
        print(f"Competitor \n {set[competitor]}")
        print(f"You \n {set[player]} You Win!")
    