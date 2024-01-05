a=[0 for _ in range(30)]

for _ in range(28):
    num=int(input())
    a[num-1]=num

for i in range(30):
    if a[i]==0:
        print(i+1)