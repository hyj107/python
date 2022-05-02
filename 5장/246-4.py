#성적의 등급을 계산하는 함수

def getGrade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
        
    return grade    

s=int(input("점수를 알려줘"))
print("성적은",getGrade(s),"입니다.")
