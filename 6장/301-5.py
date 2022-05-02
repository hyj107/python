#문자열에서 특정 패던 찾는 프로그램

lst=["aba","xyz","abc","121"]
cnt = 0

for i in lst:
    if i[0] == i[-1]:
        cnt = cnt+1
        # print(i)

print(cnt)

#함수를 사용
def test():
    cnt = 0
    for i in lst:
        if i[0] == i[-1]:
            cnt = cnt+1
            return cnt
            # print(i)


lst=["aba","xyz","abc","121"]


print(test())                