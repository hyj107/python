# 248p 13번
import random

def dice_came():
    x=random.randint(1,7)
    y=random.randint(1,7)
    print("인간: 주사위값=",x)
    print("컴퓨터: 주사위값=",y)
    
    if x>y:
        msg="인간승리"
    elif x<y:
        msg="컴퓨터 승리"
    else:
        msg="무승부"
    return msg

c=False

while c == False:
    print("======= dice_game() 호출 =======")
    print(dice_came())
    print("======= dice_game() 복귀 =======")
    n =input("중단할까요? Y/N")
    if n == "Y" :
        break