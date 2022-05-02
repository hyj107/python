# p.110 프로그래밍 01번

x=int(input("x:"))
y=int(input("y:"))

sum= x+y
MINUS= x-y
MULT= x*y
AVER= 1/2*(sum)

print("두수의 합:", sum)
print("두수의 차:", MINUS)
print("두수의 곱:", MULT)
print("두수의 평균", AVER)
print("큰수",max(x, y))
print("작은수",min(x, y))