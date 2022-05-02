# -*- coding: utf-8 -*-
"""
150p.5번 4개의 정수를 입력받아 제일 작은 정수 판별
"""

a, b, c, d = eval(input("4개의 정수를 입력하시오:"))

if a <= b :
    min1 = a
else :
    min1 = b
    
if c <= d :
    min2 = c
else :
    min2 = d
    
if min1 <= min2 :
    ttt = min1 
else :
    ttt = min2
    
print(ttt)



x,y =eval(input"")


if x > y:
    x=max
    y=min
else 
