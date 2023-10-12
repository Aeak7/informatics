# ---------------------------------------------------------------
# This program reads in an input image (PGM format), computes its
# statistics, performs image modification, and then writes out the
# outcome image
# It also prompts the user for the input filename to be used.
#
# Edited by Abby Kelly
# October 11, 2023
# Note:  It imports the math library in order to use the sqrt() 
#        function
# ---------------------------------------------------------------

import math
import copy
from functions import *

# entrance message and first input
print("Welcome to the Image Statistical Analysis and Processing program.")
filename = input("Please enter an input filename (without the .pgm): ")

# ----------------------------------------------
# open and read from the input image file
# stores the image into the 2D array 'raster'
# ----------------------------------------------
raster = []
readInFile(filename, raster)

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
choice = input("Please select an effect for your image (invert, darken, lighten): ")
modifyImage(choice, numRows, numCols, raster, maxVal, average)

# ----------------------------------------------
# open and write to the output image file
# ----------------------------------------------
writeOutFile(filename, raster)

# exiting message
print("Thank you for using the Image Statistical Analysis and Processing program.")



