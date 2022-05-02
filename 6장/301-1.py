#입력한 값을 합계내는 프로그램

kkk=[]

cnt=int(input("입력할 값의 갯수:"))

for i in range(cnt):
    x = int(input("값을 입력"))
    kkk.append(x)
    
print(sum(kkk))
