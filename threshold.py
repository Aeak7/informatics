#
# Abigail Kelly
# A quick method to get information on which data points are greater than a threshold, allowing
# for transfer into excel
#

import csv

threshold = 1 # the lowest number allowed to be in the temperature column
filePath = 'informatics/STEP4FINAL.csv' # Please select your filepath to open here, as different people have their files set up differently

with open(filePath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  next(csvreader)
  for row in csvreader:
    if(float(row[2]) > threshold): # checks if the temperature change is above 1
      print(row[2]) 
      #print(row[3]) # choose to print either the temperature or the poverty column to them copy over into excel