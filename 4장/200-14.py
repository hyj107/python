# 200p. 14번

for i in range(2,21):
    result=True
    if i<2:
        result=False
    for j in range(2,i):
        if i%j==0:
            result=False
    if result:
        print(i,end=" ")