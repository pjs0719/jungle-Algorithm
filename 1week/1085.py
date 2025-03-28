x,y,w,h = map(int, input().split())

min = x - 0

if min > (w - x):
    min = w - x 
if min > (y - 0):
    min = y - 0
if min > (h - y):
    min = h - y


print(min)

#min 함수에 다 넣어도 가능
