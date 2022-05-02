# 153p. 15

x=int(input("정수를 입력하시오:"))

if x%3==0 and x%5==0:
    msg="Python Express"
elif x%3==0:
    msg="Python"
elif x%5==0:
    msg="Express"

print(msg)

