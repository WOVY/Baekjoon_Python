N,X=map(int,input().split())
a=map(int,input().split())    
a=list(a)
for i in range(N):
    if a[i]<X:
        print(a[i])