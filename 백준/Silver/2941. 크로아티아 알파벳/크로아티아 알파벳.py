S=input()
sum=0
i=0
j=0
while True:
    i=i+j
    if i==len(S): break
    j=1
    while True:
        if S[i:i+j]=="c=":
            sum+=1
            break
        elif S[i:i+j]=="c-":
            sum+=1
            break
        elif S[i:i+j]=="dz=":
            sum+=1
            break
        elif S[i:i+j]=="d-":
            sum+=1
            break
        elif S[i:i+j]=="lj":
            sum+=1
            break
        elif S[i:i+j]=="nj":
            sum+=1
            break
        elif S[i:i+j]=="s=":
            sum+=1
            break
        elif S[i:i+j]=="z=":
            sum+=1
            break
            
        if j==3:
            j=1
            sum+=1
            break

        j+=1

print(sum)