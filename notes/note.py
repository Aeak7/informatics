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

# review for midterm:
# ------------------------
# computational thinking
# design thinking
# creative thinking
# statistical thinking
#   central tendency(avg, mode), disribution(how distributed over range), dispersion(how far data is away)
#   correlated or not correlated variables
# file i/o

# how to determine p-value when testing null hypothesis
#   come up with something you want to prove wrong
#   null hypothesis typical: the thing being studied produces no effect
# type 1 error: rejection of null with conclusion that effect exists when it doesnt (false positive)
# type 2 error: failure to reject a false null (false negative)
# p-value: critical value, look up z-table to find
#   find probability that z is beyond (more-extreme) test statistic
# ex: claim: 25% of ppl at UNL are husker fans. survey says 20% of 100 ppl are fans
#   standard error: p=0.20, sq(p(1-p)/n) = 4%
#   test statistic: (0.20-0.25) / 0.04 = -1.25 (tells you how far you are away from mean)
#   hypothesis was p=0.25, z-table look up: 0.1056, is this significant? <0.1(*), <0.05(**), <0.01(***) lower is more significant
#   0.1 value is not significant enough 