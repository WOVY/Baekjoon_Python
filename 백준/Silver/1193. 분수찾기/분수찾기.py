X = int(input())
i = 1
ind = 1
while True:
    if ind + i > X:
        break
    ind += i
    i += 1
if i % 2 == 0:
    a = 1
    b = i
    while ind != X:
        ind += 1
        a += 1
        b -= 1
elif i % 2 != 0:
    a = i
    b = 1
    while ind != X:
        ind += 1
        a -= 1
        b += 1

print(a, b, sep='/')
