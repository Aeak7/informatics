# returns user-inputted first choice
# validates that the input is an int and is between 1 to 4
def validateInitialChoice(choice):
  while True:
    try:
      choice = int(input())
    except:
      print("Please use numeric digits")
      continue
    if choice > 4 or choice < 1:
      print("Please enter 1, 2, 3 or 4")
      continue
    break
  return choice

# returns user-inputted threshold, validating that it is an int
def validateThreshold():
  threshold = 0
  while True:
    try:
      threshold = int(input())
    except:
      print("Please use numerical whole digits")
      continue
    if threshold < 0:
      print("Please enter a positive number")
      continue
    break
  return threshold

# returns user-inputted threshold, validating that the string matches with the array of acceptable values
def validateCategory(list):
  threshold = str(input())
  if threshold not in list:
    print("That doesn't match a category, please try again")
    quit()
  else:
    return threshold

# handles end result printing 
def printEndResults(choice, count, threshold):
  if(choice == 1):
    print("There are " + str(count) + " out of 100 Instagram accounts that have over " + str(threshold) + " million followers!")
  elif(choice == 2):
    print("There are " + str(count) + " out of 100 Instagram accounts that are categorized under " + str(threshold))
  elif(choice == 3):
    print("There are " + str(count) + " out of 100 Instagram accounts that have over " + str(threshold) + " media posts!")
  elif(choice == 4):
    print("There are " + str(count) + " out of 100 Instagram accounts that are categorized under " + str(threshold))
  else:
    print("Choice is invalid")
