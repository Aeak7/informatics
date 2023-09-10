import csv
from functions import *

choice = 1
threshold = 100

count = 0

with open('./mostFollowed.csv', 'r') as csv_infile:  
  data_reader = csv.reader(csv_infile, delimiter=',') 
  for row in data_reader:  
    if(choice == 1): 
      if float(row[2]) > threshold:
        count += 1
    elif(choice == 2): 
      if row[4] == threshold:
        count += 1
    elif(choice == 3): 
      if float(row[7]) > threshold:
        count += 1
    else:
      print("you dummy")

printEndResults(choice, count, threshold) 
print("Thank you for using the Instagram Data Analyzer. Goodbye!")
