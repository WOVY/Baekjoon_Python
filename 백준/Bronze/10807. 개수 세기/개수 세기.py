N=int(input())
a = list(map(int,input().split()))
s=0
v=int(input())
for i in range(N):
    if a[i]==v:
        s+=1

print(s)