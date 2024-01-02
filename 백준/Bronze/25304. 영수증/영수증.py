X=int(input()) #영주증에 적힌 총 금액
N=int(input()) #영수증에 적힌 구매한 물건의 종류의 수
S=0
for i in range(N):
    A,B=map(int,input().split())
    S+=(A*B)

if X==S:
    print("Yes")
else:
    print("No")