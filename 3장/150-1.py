# 150p 1번

x=int(input("정수를 입력하세요:"))
y=int(input("정수를 입력하세요:"))

if x % y == 0:
    msg="약수입니다."
else:
    msg="약수가 아닙니다."
    
print(msg)