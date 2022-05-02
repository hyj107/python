# 153p. 14

a=float(input("a를 입력하시오:"))
b=float(input("b를 입력하시오:"))
c=float(input("c를 입력하시오:"))

r=b**2-4*a*c

if r>0:
     msg="2개의 실근을 갖습니다."
     x1 = (-b + r**0.5) / (2*a)
     x2 = (-b - r**0.5) / (2*a)
     s=("실근은{}과{}입니다".format(x1, x2))
    
elif r==0:
    msg="중근입니다."
    x = -b / 2*a
    s=("중근은{}입니다.".format(x))
    
else:
    msg="해가 없습니다."
     
print(msg)
print(s)