#200p 13번

n=int(input("몇 번째 항까지 구할까요?"))

list = [] 
for x in range(0,n): 
    if x < 2: 
        list.append(1) 
    else: 
        list.append(list[x-2] + list[x-1]) 
print(*list)
