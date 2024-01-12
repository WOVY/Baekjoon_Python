A=[0 for _ in range(9)]
for i in range(9):
    A[i]=list(map(int,input().split()))
max=-1
for j in range(9):
    for k in range(9):
        if A[j][k]>max:
            max=A[j][k]
            max_j=j+1
            max_k=k+1

print(max)
print(max_j,max_k)