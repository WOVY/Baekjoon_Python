N,M=map(int,input().split())
a=[]
for i in range(N):
    a.append(0)
for _ in range(M):
    i,j,k=map(int,input().split())
    
    if N==1:
        a[0]=k
    else:
        for q in range(i-1,j):
            a[q]=k
for i in range(N):
    print(a[i],end=' ')