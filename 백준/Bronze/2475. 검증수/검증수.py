def f(a,b,c,d,e):
    sum=a**2+b**2+c**2+d**2+e**2
    return sum%10
    
a,b,c,d,e=map(int,input().split())
print(f(a,b,c,d,e))