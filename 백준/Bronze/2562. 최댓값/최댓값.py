a=[]
for i in range(9):
    a.append(int(input()))
max=a[0]
max_i=1
for i in range(1,9):
    if max<a[i]:
        max=a[i]
        max_i=i+1
        
print(max,max_i)