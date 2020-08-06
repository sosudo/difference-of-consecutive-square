x = -99999999999999999
y = x + 1
while(True):
  if ((y*y) - (x*x) == x + y):
    print("True")
    continue
  else:
    print("False")
    break
  x+=1
  y+=1