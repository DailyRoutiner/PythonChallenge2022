#from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)
peopleDictionary = []
flag = "yes"

def findWinner(peopleDic):
  maxBid = 0
  winnerName = ""
  
  for onePerson in peopleDic:
    if maxBid < onePerson["Price"]:
      maxBid = onePerson["Price"]
      winnerName = onePerson["Name"]
  print(f"Winner is {winnerName} Price is {maxBid}")

while flag == "yes":
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  peopleDictionary.append({"Name": name, "Price": price})
  
  print(peopleDictionary)
  
  flag = input("If there are other users who want to bid?").lower()
  if flag =="yes":
    #clear() 
    1
  else:
    findWinner(peopleDictionary)





