# 246p 5번
import string
alphalower = string.ascii_lowercase
alphaupper = string.ascii_uppercase
digs = string.digits

def checkPass():
    global x
    
    if len(p) >= 8 and p.count(digs) >= 1 and p.count(alphaupper) >= 1 and p.count(alphalower) >= 1:
        x=True
       
    else:
        x=False
        

x=False

while x==False:
    p=input("패스워드를 입력하시오:")
    checkPass()
    if x == True:
        print("사용할 수 있습니다.")
        
    else:
        print("사용할 수 없습니다.다시 입력하세요")


#리턴이 안됨   
        
