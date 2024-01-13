A=[[-1]*16 for _ in range(5)]
for i in range(5):
    S=input()
    for j in range(len(S)):
        A[i][j]=S[j]

for i in range(16):
    for j in range(5):
        if A[j][i]!=-1:
            print(A[j][i],end='')