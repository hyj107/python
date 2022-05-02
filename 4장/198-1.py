# 2부터 50사이의 짝수

start=int(input("시작값:"))
end=int(input("끝값:"))

if start%2==1:
    start=start+1

cnt= 0
for x in range(start, end+1, 2):
    print(x, end=" ")
    cnt=cnt+1
    
print()    
print("짝수의 갯수:",cnt)