# 리스트의 합을 구하는 프로그램

myList=[11,122,23,-99,281,93,135]

start=int(input("범위의 시작값="))
end=int(input("범위의 끝값="))

sum = 0

for i in myList :
    if i > start and i < end :
        sum = sum+i

print("리스트에서 30보다 크고 100보다 작은 합 =",sum)