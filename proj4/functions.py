def modifyImage(choice, numRows, numCols, imageArray, highIntensity, average):
# inverts the colors of the image, useful to view the image from a different perspective for finding discrepancies, similar to viewing an xray image
  if choice == "invert":
    for x in range(0, numRows - 1):
        for y in range(0, numCols - 1):
          imageArray[x][y] = highIntensity - imageArray[x][y]
    print(f"--> Inverted.")
# subtracts the avg from the default, making the image significantly darker, perfect for spooky images
  elif choice == "darken": 
    for x in range(0, numRows - 1):
        for y in range(0, numCols - 1):
          imageArray[x][y] = imageArray[x][y] - average
    print(f"--> Darkened.")
  # the opposite of darken, adds the avg, making the image much easier to see on dimmer screens, particularly useful for my terribly dim monitor
  elif choice == "lighten": 
    for x in range(0, numRows - 1):
        for y in range(0, numCols - 1):
          imageArray[x][y] = imageArray[x][y] + average
    print(f"--> Lightened.")
  else:
    print("Invalid Input")

def readInFile(filename, imageArray):
    # -- 1. read the image header
  inputFile = open('informatics/proj3/images/'+filename+'.pgm','rb')  # open up the input file so we can read from it
  inputFile.readline()  # read the comment line #1
  inputFile.readline()  # read the comment line #2
  (width, height) = [int(i) for i in inputFile.readline().split()]
  depth = int(inputFile.readline())
  # -- 2. read in the image, one byte at a time    
  for y in range(height):
      row = []
      for y in range(width):
          row.append(ord(inputFile.read(1)))
      imageArray.append(row) 
  inputFile.close()  # close the file

def writeOutFile(filename, imageArray):
  numRows = len(imageArray)
  numCols = len(imageArray[0])
  # -- 1. write out the image header
  outputFile = open('informatics/proj3/images/'+filename+'out.pgm','w')
  outputFile.write("P2\n")
  outputFile.write("# output image\n")
  outputFile.write("" + str(numRows) + " " + str(numCols) + "\n")
  outputFile.write("255\n")
  # -- 2. write out the image
  for x in range(0,numRows):
    for y in range(0,numCols):
        outputFile.write(""+str(imageArray[x][y])+" ")
