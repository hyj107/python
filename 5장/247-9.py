# 247p 9번 

def gcd(x, y): 
    if x < y: (x, y) = (y, x) 
    while y != 0: 
        (x, y) = (y, x % y) 
    return x


x=int(input("첫 번째 정수:"))
y=int(input("두 번째 정수:"))
gcd(x, y)

s=gcd(x,y)
print(s)