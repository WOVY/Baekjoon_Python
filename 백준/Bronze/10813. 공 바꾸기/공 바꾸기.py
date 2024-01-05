N,M=map(int,input().split())
a=[]
for i in range(1,N+1):
    a.append(i)

for _ in range(M):
    i,j=map(int,input().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]

for i in range(N):
    print(a[i],end=' ')