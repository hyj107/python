# 가위바위보

import random

computer_choice = random.randrange(1,4)

human = int(input("선택하시오(1:가위 2:바위 3:보)"))
print("컴퓨터의 선택(1:가위 2:바위 3:보)",computer_choice)

if computer_choice == human:
    msg="비겼습니다."

else :
    if human == 1 :
        if computer_choice ==3:
            msg="인간 승"
        else :
            msg="컴퓨터 승"
    
    if human == 2 :
         if computer_choice ==1:
            msg="인간 승"
         else :
             msg="컴퓨터 승"
    
    if human == 3 :
        if computer_choice ==2:
             msg= "인간 승"
        else:
            msg="컴퓨터 승"
            
print(msg)
