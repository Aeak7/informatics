# comment
print("Hello World")

threshold = 100

var1 = float(input("Please enter number: "))
var2 = float(input("Please give 2nd num: "))
var3 = var1 + var2
print("Here is the number: " + str(var3)) #cannot print ints/floats

# if (var3 > threshold):
#   print("Greater than threshold")
# elif (var3 < threshold):
#   print("Less than threshold")
# elif (var3 == threshold):
#   print("Equal to threshold")
# else:
#   print("Else case")

#not && and || but rather and and or

if (var3 > threshold):
  print("Greater than")
else:
  print("Not greater")

items = ["dog", "cat", "lizard"]
for item in items: # do stuff, like a js loop
  print(item)

for i in range(5): # range(0,10), range(0,15,3) --> increment by 3
  print("hi")

# arrays
x = items[0]
items[0] = "bug"
x = len(items)
items.append("elephant")
items.pop(0)
items.remove("cat")

# image[row][column]
# x==y
# (x>y)

# colors inverted
for x in range(0, numRows - 1):
  for y in range(0, numCols - 1):
    raster[x][y] = maxVal - raster[x][y]