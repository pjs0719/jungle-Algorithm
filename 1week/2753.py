year = int(input())

if 0 == year%4 and ((0 != year%100) or (0 == year%400)):
    print("1")
else:
    print("0")


