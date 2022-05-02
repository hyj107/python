# 248p 12번

def getSortes(x,y):
    if x>y:
        max=x
        min=y
    elif x<y:
        max=y
        min=y
    else:
        max,min=x,y
    return max, min

x=int(input("첫 번째 정수:"))
y=int(input("두 번째 정수:"))

a,b=getSortes(x,y)
print(b,a)

