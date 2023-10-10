# ---------------------------------------------------------------
# This program reads in an input image (PGM format), computes its
# statistics, performs image modification, and then writes out the
# outcome image
# It also prompts the user for the input filename to be used.
#
# Edited by Abby Kelly
# September 25, 2022
# Note:  It imports the math library in order to use the sqrt() 
#        function
# ---------------------------------------------------------------

import math
import copy
from functions import *

# ----------------------------------------------
# print out welcome message
# ----------------------------------------------
print("Welcome to the Image Statistical Analysis and Processing program.")

# ----------------------------------------------
# prompt the user for the input filename
# ----------------------------------------------
filename = input("Please enter an input filename (without the .pgm): ")

# ----------------------------------------------
# open and read from the input image file
# store the image into the 2D array 'raster'
# ----------------------------------------------
# -- 1. read the image header
inputFile = open('proj3/images/'+filename+'.pgm','rb')  # open up the input file so we can read from it
inputFile.readline()  # read the comment line #1
inputFile.readline()  # read the comment line #2
(width, height) = [int(i) for i in inputFile.readline().split()]
depth = int(inputFile.readline())

# -- 2. read in the image, one byte at a time    
raster = []  # image stored here
for y in range(height):
    row = []
    for y in range(width):
        row.append(ord(inputFile.read(1)))
    raster.append(row) 
inputFile.close()  # close the file

# check if input file is read in correctly, set up rows and columns
numRows = len(raster)
numCols = len(raster[0])
print("number of rows", len(raster))
print("number of columns", len(raster[0]))

# ----------------------------------------------
# Compute four statistics
# ----------------------------------------------
# 1. Average Intensity
total = 0
for x in range(0, numRows):
  for y in range(0, numCols):
     total += raster[x][y] # add each individual value together
average = total / (numRows * numCols) # divide by total size of raster to find mean
print(f"average intensity: {average}")

# 2. Lowest Intensity
minVal = []
for x in range(0, numRows):
  for y in range(0, numCols):
     minVal.append(raster[x][y]) # placing all values of raster into minVal
minVal = min(minVal) # with all the individual values out of raster, use min() function to find minimum value
print(f"lowest intensity: {minVal}")

# 3. Highest Intensity
maxVal = []
for x in range(0, numRows):
  for y in range(0, numCols):
     maxVal.append(raster[x][y]) # place all values of raster into maxVal
maxVal = max(maxVal) # now we have individual numbers, can use max() to find maximum number in the list
print(f"highest intensity: {maxVal}")

# 4. Standard Deviation of Intensity of Image
# stdev = sqrt(sum((values - mean)^2) / size)
summed = 0
rasterCopy = copy.deepcopy(raster) # copied raster so the output picture is not affected by calculations. Is a bit slow...
for x in range(0, numRows):
  for y in range(0, numCols):
     rasterCopy[x][y] = pow((rasterCopy[x][y] - average), 2) # do the very interior of equation first, (values - mean)^2
     summed += rasterCopy[x][y] # slowly work out from the interior of equation, sum all the new values together
stdev = (summed / (numRows * numCols)) ** 0.5 # divide all the summed values by the size of raster, and sqrt it
print(f"stdev of intensity: {stdev}")

# ----------------------------------------------
# Modification of Image
# ----------------------------------------------
# Added an input question so each effect isn't interfering with the others
# Similar to the copy created for the stdev so it wouldn't affect these effects
choice = input("Please select an effect for your image (invert, darken, lighten): ")
if choice == "invert":
   invertImageColors(numRows, numCols, maxVal, raster)
   print(f"--> Inverted. Find image at: {filename}out.pgm")
# subtracts the avg from the default, making the image significantly darker, perfect for spooky images
elif choice == "darken": 
   for x in range(0, numRows - 1):
      for y in range(0, numCols - 1):
         raster[x][y] = raster[x][y] - average 
   print(f"--> Darkened. Find image at: {filename}out.pgm")
# the opposite of darken, adds the avg, making the image much easier to see on dimmer screens, particularly useful for my terribly dim monitor
elif choice == "lighten": 
   for x in range(0, numRows - 1):
      for y in range(0, numCols - 1):
         raster[x][y] = raster[x][y] + average
   print(f"--> Lightened. Find image at: {filename}out.pgm")
else:
   print("Invalid Input")

# ----------------------------------------------
# open and write to the output image file
# ----------------------------------------------
# -- 1. write out the image header
outputFile = open('proj3/images/'+filename+'out.pgm','w')
outputFile.write("P2\n")
outputFile.write("# output image\n")
outputFile.write("" + str(numRows) + " " + str(numCols) + "\n")
outputFile.write("255\n")

# -- 2. write out the image
for x in range(0,numRows):
   for y in range(0,numCols):
      outputFile.write(""+str(raster[x][y])+" ")

# ----------------------------------------------           
# Display an exit message
# ----------------------------------------------
print("Thank you for using the Image Statistical Analysis and Processing program.")



