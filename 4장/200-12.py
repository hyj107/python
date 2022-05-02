# 200p 12번

import random
count=0
for i in range(10000000):
    x=random.uniform(0,1.0)
    y=random.uniform(0,1.0)
    if (x**2+y**2)<=1:
        count=count+1
print("파이의 값은 ",4*count/10000000,"입니다.")