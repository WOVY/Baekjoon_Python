N=int(input())
a=list(map(int,input().split()))
max=max(a)
for i in range(N):
    a[i]=(a[i]/max)*100
sum=0
for i in range(N):
    sum+=a[i]
print(format(sum/N,".2f"))