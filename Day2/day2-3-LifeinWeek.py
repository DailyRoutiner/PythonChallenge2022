# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leftAge = 90 - int(age)

day = 365 * leftAge
week = 52 * leftAge
month = 12 * leftAge
print(f"You have {day} days, {week} weeks, and {month} months left.")