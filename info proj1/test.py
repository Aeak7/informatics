from functions import *

print("Welcome to the Instagram Data Analyzer!")
print("Please select one of the following options: ")
print("1: Count the number of accounts with over ___ million followers")
print("2: Count the number of accounts in a particular category")
print("3: Count the number of accounts with over ___ media posts")

while True:
    try:
      choice = int(input("Please enter your option: "))
    except:
      print("Please use numeric digits")
      continue
    if choice > 3 or choice < 1:
      print("Please enter 1, 2 or 3")
      continue
    break

if(choice == 1):
  print("You chose option 1\nPlease enter the threshold value (Followers in Millions): ")
  threshold = validateThreshold()
elif(choice == 2):
  print("You chose option 2\nEnter keyword from: (beauty, beverages, celebrities, entertainment, fashion, media, other, sport): ")
  threshold = str(input())
elif(choice == 3):
  print("You chose option 3\nPlease enter the threshold value (Media Posts): ")
  threshold = validateThreshold()
else:
  print("Choice was not 1,2,or 3")