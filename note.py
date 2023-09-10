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