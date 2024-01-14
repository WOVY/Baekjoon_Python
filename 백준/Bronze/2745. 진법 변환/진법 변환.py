N,B=input().split()
B=int(B)
L=len(N)
sum=0
for i in range(L):
    n=ord(N[i])
    if n>=48 and n<=57:
        sum+=(n-48)*(B**(L-i-1))
    else:
        sum+=(n-55)*(B**(L-i-1))
        
print(sum)