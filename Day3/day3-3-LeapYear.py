# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leap = 0

if year % 4 == 0:
    leap += 1
    if year % 100 != 0:
        leap += 1
        if year % 400 == 0:
            leap += 1

if leap >= 2:
    print("Leap year.")
else:
    print("Not leap year.")


