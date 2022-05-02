# 사칙연산을 자동으로 생성하는 프로그램

import random

x= random.randint(1,100)
y= random.randint(1,100)

choice= random.randint(1,4)

if choice == 1:
    result = x + y
    kid=int(input(f"{x}+{y}="))
   
elif choice == 2:
    result = x - y
    kid=int(input(f"{x}-{y}="))
    
elif choice == 3:
    result = x * y
    kid=int(input(f"{x}*{y}="))
else:
    result = x / y
    kid=int(input(f"{x}//{y}="))


if kid == result:
    print("참 잘했어요!")
else :
    print("다시 해보세요")

