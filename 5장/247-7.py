# 247p 7번

print("날짜를 입력하시오(월과 일)")

x=False
y=False

while x==False:
    M=int(input("월을 입력하시오(1부터 12사이의 값):"))
    if 1 <= M <= 12:
        x=True
    else:
        x=False

while y==False:
    D=int(input("일을 입력하시오(1부터 31사이의 값):"))
    if 1 <= D <= 31:
        y=True
    else:
        y=False

print(f"입력된 날짜는 {M}월{D}일입니다.")

