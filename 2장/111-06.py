# -*- coding: utf-8 -*-
"""
2장 프로그래밍 6번 문제풀이
작성자: 황유진
작성일: 2021년 3월 29일
"""
#음식 비용과 팁 비율을 입력 받아 각각 cost와 tip에 값을 저장
cost=int(input("음식 비용을 입력하세요:"))
tip=int(input("팁 비율을 입력하세요:"))

#입력 받은 값을 계산해 total에 저장
total=cost+cost*tip/100

#입력 받은 값과 계산한 값을 모두 출력
print(f"\n 음식비용:{cost}\n 팁 비율:{tip}\n 총액:",int(total),"달러")