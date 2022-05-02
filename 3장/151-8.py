# 151p. 8번

x,y=map(int,input("체중과 키를 입력하시오:").split())

stn=(x-100)*0.9

if y==stn:
    msg="표준입니다."
elif y>=stn:
    msg="과체중입니다."
else:
    msg="저체중입니다."

print(msg)



