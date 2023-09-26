# ---------------------------------------------------------------
# This program reads in an input image (PGM format), computes its
# statistics, performs image modification, and then writes out the
# outcome image
# It also prompts the user for the input filename to be used.
#
# Written by Leen-Kiat Soh
# September 15, 2022
# Note:  It imports the math library in order to use the sqrt() 
#        function
# ---------------------------------------------------------------

import math

# ----------------------------------------------
# print out welcome message
# ----------------------------------------------
# enter code here

# ----------------------------------------------
# prompt the user for the input filename
# ----------------------------------------------
# enter code here

# ----------------------------------------------
# open and read from the input image file
# store the image into the 2D array 'raster'
# ----------------------------------------------
# -- 1. read the image header
inputFile = open('images/'+filename+'.pgm','rb')  # open up the input file so we can read from it
inputFile.readline()  # read the comment line #1
inputFile.readline()  # read the comment line #2
(width, height) = [int(i) for i in inputFile.readline().split()]
depth = int(inputFile.readline())

# -- 2. read in the image, one byte at a time    
raster = []  # this is where we store the image
for y in range(height):
    row = []
    for y in range(width):
        row.append(ord(inputFile.read(1)))
    raster.append(row)
    
inputFile.close()  # close the file

# just to check whether we read the input file correctly
# also to setup the number of rows and number of columns correctly
numRows = len(raster)
numCols = len(raster[0])
print("number of rows", len(raster))
print("number of columns", len(raster[0]))


# ----------------------------------------------
# Compute four statistics
# ----------------------------------------------
# 1. Compute the average intensity of the iamge
# 2. Compute the lowest intensity of the image
# 3. Compute the highest intensity of the image
# 4. Compute the standard deviation of the intensity of the image
# enter code here


# ----------------------------------------------
# Use at least two of the statistics computed above to modify the image
# Describe your design and the purpose of your "modification" (10 points)
# ----------------------------------------------
# -- what effects does your modification achieve?
# enter code here


# ----------------------------------------------
# open and write to the output image file
# ----------------------------------------------
# -- 1. write out the image header
outputFile = open('images/'+filename+'out.pgm','w')
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
# Enter code here



