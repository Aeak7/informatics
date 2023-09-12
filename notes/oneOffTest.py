evenValue = False
x = 0
sum = 0

while (not evenValue) and (x < 100):
  x = int(input())
  if (x % 2 == 0):   # what does the operator "%" do?
    evenValue = True
    sum = sum + x
  else:
    sum = sum - x

print(sum)
   # end if
# end while