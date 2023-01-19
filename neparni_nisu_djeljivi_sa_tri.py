while 1:
    n = int(input("Unesi cijeli broj: "))
    if n>0:
        break
for i in range(1,n+1,2):
    if i%3!=0:
        print(i)
