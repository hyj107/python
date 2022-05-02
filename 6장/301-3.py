# 리스트의 값을 *로 출력하는 프로그램

lst=[]

for x in range(5):
    lst.appand(int(input("점수 5개 입력")))

for i in lst:
    print(i,"\t", "*"* i)
    
