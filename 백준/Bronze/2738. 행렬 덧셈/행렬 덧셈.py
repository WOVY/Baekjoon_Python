N,M=map(int,input().split())
A=[0 for _ in range(N)]
for i in range(N):
    A[i]=list(map(int,input().split()))
B=[0 for _ in range(N)]
for j in range(N):
    B[j]=list(map(int,input().split()))

for k in range(N):
    for l in range(M):
        print(A[k][l]+B[k][l], end=' ')
    print()