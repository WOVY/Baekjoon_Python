S=input()
a=[0 for _ in range(26)]
for i in range(len(S)):
    if ord(S[i])>=65 and ord(S[i])<=90:
        a[ord(S[i])-65]+=1
    else:
        a[ord(S[i])-97]+=1
m=max(a)
idx=a.index(m)
if a.count(m)>1:
    print("?")
else:
    print(chr(idx+65))