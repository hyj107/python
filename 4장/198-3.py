#1부터 100까지의 3의 배수의 합
sum=num=0

for i in range(1, 101):
    if i %3==0:
        sum= sum+i
        num= num+1
        
print(sum, num)