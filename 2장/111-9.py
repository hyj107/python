#111p 9번

x=int(input("4자리 정수를 입력하시오:"))

sum=0

num1=x//1000
num2=x%10
num3=(x//100)%10
num4=(x%100)//10
sum=num1+num2+num3+num4

print(sum)