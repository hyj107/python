# 난수 10갤 만들어 리스트에 저장

import random
values = []

for i in range(10):
    values.append(random.randint(1,101))
    
print(values)

for v in values:
    print(v,end=" ")