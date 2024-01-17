S=input().split()
S=list(map(int,S))

if S[0]==1:
    for i in range(len(S)-1):
        if S[i+1]==S[i]+1:
            pass
        else:
            print("mixed")
            exit(0)
    print("ascending")
else:
    for j in range(len(S)-1):
        if S[j+1]==S[j]-1:
            pass
        else:
            print("mixed")
            exit()
    print("descending")