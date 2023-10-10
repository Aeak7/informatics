def process2(a,b):
   val = b - a
   return val

def process(a,b):
   a = 7
   b = 10
   val = process2(b,a) + a
   return val


a = 1
b = 2
print(str(process(b,a)))