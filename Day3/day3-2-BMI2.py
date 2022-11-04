# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)

if bmi < 18.5:
    result = "you are underweight"
elif bmi < 25:
    result = "you have a normal weight"
elif bmi < 30:
    result = "you are slightly overweight"
elif bmi < 35:
    result = "you are obese"
else:
    result = "you are clinically obese"


print(f"Your BMI is {round(bmi)}, {result}.") 