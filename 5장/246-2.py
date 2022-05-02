# 246p 2번

def main(x,y):
    add=x+y
    sud=x-y
    mul=x*y
    div=x/y
    print(f"({x}+{y})={add} \n({x}-{y})={sud} \n({x}*{y})={mul} \n({x}/{y})={div}")
    
x=int(input("첫 번째 정수 입력:"))
y=int(input("두 번째 정수 입력:"))
main(x,y)   