# 152p. 12번

x=int(input("연도를 입력하시오:"))

if x%12==0:
    msg="원숭이띠입니다."
elif x%12==1:
    msg="닭띠입니다."
elif x%12==2:
    msg="개띠입니다."
elif x%12==3:
    msg="돼지띠입니다."
elif x%12==4:
    msg="쥐띠입니다."
elif x%12==5:
    msg="소띠입니다."
elif x%12==6:
    msg="호랑이띠입니다."
elif x%12==7:
    msg="토끼띠입니다."
elif x%12==8:
    msg="용띠입니다."
elif x%12==9:
    msg="뱀띠입니다."
elif x%12==10:
    msg="말띠입니다."
elif x%12==11:
    msg="양띠입니다."
    
print(msg)