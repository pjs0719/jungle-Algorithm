
for _ in range(int(input())):
    good = 0
    score = list(map(int, input().split()))
    mean = sum(score[1:]) / score[0]
    for i in score[1:]:
        if i > mean:
            good += 1
    Percent = (good/score[0])*100
    
    print("%.3f%%" % Percent )
    
    

#슬라이스, 소숫점 지정
    
