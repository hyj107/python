#246p 3번

def test(x,y):
    add=x+y
    sud=x-y
    mul=x*y
    div=x/y
    return add,sud,mul,div

    
x=int(input("첫 번째 정수 입력:"))
y=int(input("두 번째 정수 입력:"))
test(x,y)   

a,b,c,d = test(x,y)
print(a,b,c,d,"이 반환되었습니다.")