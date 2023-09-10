x = 10
y = 3
z = 2

output = 0
if (x >= 3):
  output = 5
elif (y < 4) and (z < 3):
  output = 6
elif (z >= 3):
  output = 7
  if (y < 4):
    output = 8

print(output)