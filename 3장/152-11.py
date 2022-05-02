# 153p 11번

k=eval(input("무게(킬로그램):"))
m=eval(input("키(미터):"))

bmi=k/(m*m)

print("당신의 BMI:",bmi)

if bmi>=30:
    msg="비만입니다."
elif 25<= bmi <=29.9:
    msg="과체중입니다."
elif 20<= bmi <=24.9:
    msg="정상입니다."
else:
    msg="저체중입니다."

print(msg)