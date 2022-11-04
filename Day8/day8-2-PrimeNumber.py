#Write your code below this line 👇

def prime_checker(number):
    result1 = number % 3
    result2 = number % 2
    if result1 == 0 or result2 == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
