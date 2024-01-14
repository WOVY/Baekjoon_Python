N,B=map(int,input().split())
list=[]
while N!=0:
    D=N//B
    Q=N%B
    N=D
    list.append(Q)
list=list[::-1]
for i in range(len(list)):
    if list[i]>=10:
        list[i]=chr(list[i]+55)
for j in list:
    print(j,end='')