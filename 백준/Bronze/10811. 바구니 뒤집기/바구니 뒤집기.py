N,M=map(int,input().split())
a=[(i+1) for i in range(N)]
for _ in range(M):
    i,j=map(int,input().split())
    a=a[0:i-1]+list(reversed(a[i-1:j]))+a[j:N]

for i in range(N):
    print(a[i],end=' ')