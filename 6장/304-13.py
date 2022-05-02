table = []
number = [1,2,3,4,5,6,7,8,9,10]

def stert():
    print("-"*20)
    print( " ".join( repr(e) for e in number ) )
    print("-"*20)

def printList(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[0])):
            print(mylist[row][col], end=" ")
        print()
        
def inti(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[0])):
            table[x-1][y-1]=1


stert()

for row in range(9):
    table += [[0]*10]
      
printList(table)

x=int(input("원하시는 좌석의 행번호를 입력하세요(종료는 -1):"))
y=int(input("원하시는 좌석의 열번호를 입력하세요(종료는 -1):"))

if x==-1 or y==-1:
    msg="예약이 종료되었습니다."    
else:
    mag="예약되었습니다."

print(msg)

inti(table)
stert()
printList(table)

