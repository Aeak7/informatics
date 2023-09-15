myList = [1, 3, -5, 6, 19, 10]
something = myList[0]
count = 1

while (count < len(myList)):
  if (myList[count] > something):
    something = myList[count]
  count = count + 1

print(something)