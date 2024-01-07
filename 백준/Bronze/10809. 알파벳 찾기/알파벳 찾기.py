list1=[-1 for _ in range(26)]
s=input()
for i in range(len(s)):
    if list1[ord(s[i])-97]==-1:
        list1[ord(s[i])-97]=i

for i in range(26):
    print(list1[i], end=' ')