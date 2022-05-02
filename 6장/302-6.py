# 공통 구성원 결정 프로그램

def test():
    
    for i in list1:
        for j in list2:
            for v in list3:
                if i == j and i==v and j==v:
                #더 간단하게 i==j==v:
                    #print("True")
                    #     print(i, j)
                    return "True", i, j, v
         

list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9,10]
list3 = [2,4,6,8,10]

print(test())

#+추가 (같은 리스트 무조건 출력하는 프로그램