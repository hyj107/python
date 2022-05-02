# 윤년 계산 프로그램

year=int(input("연도를 입력하세요."))

#4로 나누어지고 100으로는 나누어지지 않거나
#400으로 나누어 지면 윤년

if (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0 ):
    msg="윤년입니다."
else :
    msg="윤년이 아닙니다."

print(msg)