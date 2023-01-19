while 1:
  n=int(input("Unesi cijeli broj:  "))
  if n>0:
    break

minimum = 9
while n!=0:
    z=n%10
    if z < minimum:
        minimum = z
    n=n//10
print(minimum)


