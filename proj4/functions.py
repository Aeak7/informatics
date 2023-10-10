# inverts the colors of the image, useful to view the image from a different perspective for finding discrepancies, similar to viewing an xray image
def invertImageColors(numRows, numCols, highIntensity, imageArray):
  for x in range(0, numRows - 1):
      for y in range(0, numCols - 1):
         imageArray[x][y] = highIntensity - imageArray[x][y]

