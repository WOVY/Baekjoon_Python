N=int(input())
a=list(map(int,input().split()))
min=a[0]
max=a[0]
for i in range(N):
    if a[i]>=max:
        max=a[i]
    elif a[i]<=min:
        min=a[i]

print(min,max)