# 248p 11번

def binary(n):
    list=[]
    
    while True:
        a=int(n/2)
        b=int(n%2)
        list.insert(0, b)
        
        if a != 0:
            n=a
        else:
            break
    final=''.join(map(str, list))
    print(final)

n=int(input("10진수: "))
binary(n)

