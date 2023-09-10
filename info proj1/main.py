# ----------------------------------------------------------------------------------------
# This program reads a CSV file, extracts its data and stores them in a set of
# arrays/lists, and then prompts the user in order to perform some basic filtering
# and counting of the data
# It reads an input CSV file called 'mostFollowed.csv'
# Authors: Abigail Kelly at UNL
# Date:  9/9/2023
# ----------------------------------------------------------------------------------------

import csv
from functions import *

# Welcome message and options
print("Welcome to the Instagram Data Analyzer!")
print("Please select one of the following options: ")
print("1: Count the number of accounts with over ___ million followers")
print("2: Count the number of accounts in a particular category")
print("3: Count the number of accounts with over ___ media posts")
print("4: Count the number of account in a particular subcategory")

# defining initial variables to carry through if and for statements
threshold = 0
choice = 0
# defining categories and subcategories for later function input
categories = ["beauty", "beverages", "celebrities", "entertainment", "fashion", "media", "other", "sport"]
subcategories = ["actors", "athletes", "basketball", "entrepreneurs", "fashion", "football", "informative",
                 "luxury", "media", "models", "musicians", "political", "retail", "other", "sport", "tv"]

choice = validateInitialChoice(choice) # calls from functions.py, validates that user-inputted choice is an int and between 1-3

# process the user-specified option
if(choice == 1): 
  print("You chose option 1\nPlease enter the threshold value (Followers in Millions): ")
  threshold = validateThreshold() # calls from functions.py, validates that user-inputted choice is an int and is positive
elif(choice == 2):
  print("You chose option 2\nEnter keyword from: (beauty, beverages, celebrities, entertainment, fashion, media, other, sport): ")
  threshold = validateCategory(categories) # calls from functions.py, validates that user-inputted choice is equal to one of the keyword options
elif(choice == 3):
  print("You chose option 3\nPlease enter the threshold value (Media Posts): ")
  threshold = validateThreshold() # calls from functions.py, validates that user-inputted choice is an int and is positive
elif(choice == 4):
  print("You chose option 4\nEnter keyword from: (actors, athletes, basketball, entrepreneurs, fashion, football, informative, luxury, media, models, musicians, political, retail, other, sport, tv): ")
  threshold = validateCategory(subcategories)

count = 0
# read the file in and process each row
with open('./mostFollowed.csv', 'r') as csv_infile:  # open up the input file
  data_reader = csv.reader(csv_infile, delimiter=',')   # attach a reading stream to get ready to read 
  for row in data_reader:   # go through each row of the data, with the data stored in the variable 'row'
    if(choice == 1): # Follower amount
      if float(row[2]) > threshold:
        count += 1
    elif(choice == 2): # In Category (String)
      if row[4] == threshold:
        count += 1
    elif(choice == 3): # Media post amount
      if float(row[7]) > threshold:
        count += 1
    elif(choice == 4):
      if row[5] == threshold:
        count += 1

printEndResults(choice, count, threshold) # print out the statistics
print("Thank you for using the Instagram Data Analyzer. Goodbye!") 