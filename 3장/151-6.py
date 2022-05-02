# 151p. 6번

import random
msg=0
computer=random.randint(1, 3)
user=int(input("선택하시오(1: 가위 2: 바위 3: 보)"))

print("컴퓨터의 선택(1: 가위 2: 바위 3: 보)",computer)

if computer == user:
    msg="비김"
elif user == 1:
    if computer == 2:
        msg="이김"
    else:
        msg="짐"
elif user == 2:
    if computer == 1:
        msg="이김"
    else:
        msg="짐"
else:
    if computer == 2:
        msg="이김"
    else:
        msg="짐" 
 
    
print(msg)