# 198p. 4번

list=[]

x=int(input("정수를 입력하시오:"))


for i in range(1,x+1):
    if x%i==0:
       list.append(i)  
        
print("약수:",*list ,end=" ")
