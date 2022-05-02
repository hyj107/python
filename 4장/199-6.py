# 199p 6번
import math

print("각도","sin값","\t","cos값")

for i in range(0,91,10):
    r=3.14*i/180.0
    s=math.sin(r)
    c=math.cos(r)
    print(i,"\t","%.3f"%s,"\t","%.3f"%c)
