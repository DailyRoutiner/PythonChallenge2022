#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇

result = random.randint(0,1)

if result == 1:
    print("Heads")
else:
    print("Tails")
