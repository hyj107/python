# 200p. 11번 

a=int(input("첫 번째 정수를 입력하시오:"))
b=int(input("두 번째 정수를 입력하시오:"))

k=2

while True:
    if a%k==0 and k%k==0:
        print(a,"과",b,"의 최대 공약수는",k,"입니다.")
        break
    else:
        k=k+1
        continue
    