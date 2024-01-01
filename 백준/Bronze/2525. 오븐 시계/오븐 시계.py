A,B=map(int,input().split())
C=int(input())

H=C//60
M=C%60

if B+M >= 60:
    if A+H+1>23:
        print(A+H+1-24,B+M-60)
    else:
        print(A+H+1,B+M-60)
else:
    if A+H>23:
        print(A+H-24,B+M)
    else:
        print(A+H,B+M)