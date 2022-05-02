# 199p 10번
sum=0
s=0

n=int(input("n의값을 입력하시오:"))

for i in range(1,n+1):
    s=i*i
    sum=sum+s

print("계산값은",sum,"입니다.")