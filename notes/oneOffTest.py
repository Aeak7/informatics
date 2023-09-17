for x in range(0,10):
  row = ""
  for y in range(0,10):
    if y == (5 - x):
      row = row + " ! "
    else:
      row = row + " * "
    
  print(row)

# 1: x == y
# 2: x > y
# 3: x != y
# 4: y == (5 - x)
# 5: y == (5 - x) or y == (13 - x) or y == (x - 5) or y == (x + 5)