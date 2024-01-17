S=input()

if S[0]=="A":
    score=4.0
    if S[1]=='+':
        score+=0.3
    elif S[1]=='-':
        score-=0.3
elif S[0]=="B":
    score=3.0
    if S[1]=='+':
        score+=0.3
    elif S[1]=='-':
        score-=0.3
elif S[0]=="C":
    score=2.0
    if S[1]=='+':
        score+=0.3
    elif S[1]=='-':
        score-=0.3
elif S[0]=="D":
    score=1.0
    if S[1]=='+':
        score+=0.3
    elif S[1]=='-':
        score-=0.3
else:
    score=0.0

print(score)