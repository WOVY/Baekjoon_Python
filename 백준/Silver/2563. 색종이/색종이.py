N=int(input())
sum=0
A=[[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x,y=map(int,input().split())
    x-=1
    y-=1
    for i in range(y+10,y,-1):
        for j in range(x,x+10):
            A[i][j]=1

for l in range(100):
    sum+=A[l].count(1)
print(sum)