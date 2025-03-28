import math

A, B, V = map(int, input().split())
days = math.ceil((V - B) / (A - B))
print(days)

#하루에 올라가는 높이 (A-B) 마지막 날에는 안미끄러져서 올라가야하는 높이는 (V-B) 




## 타임 아웃 수학식을 써야함
A, B, V = map(int, input().split())
finish = 0
days = 0
while finish < V:
    days += 1
    finish += A
    if finish >= V:
        print(days)
        break
    finish -= B
    
    

