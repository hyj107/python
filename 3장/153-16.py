# 153p. 16번

x=int(input("pH를 입력하시오:"))

if 1<=x<=6:
    msg="산입니다."
elif 8<=x<=14:
    msg="알칼리입니다."
else:
    msg="중성입니다."
