# 사용자가 문자에 따라 출력을 다르게 하는 프로그램
x = input("문자를 입력하시오:")

if x == "R" or x == "r":
    print("Rectangle")
elif x == "T" or x == "t":
    print("Triangle")
elif x == "C" or x == "c":
    print("Circle")
else :
    print("Unkwon")
