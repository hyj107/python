# 247p 10번

def testPrime():
    slist=[]
    
    for i in range(2,101):
        result=True
        if i<2:
            result=False
        for j in range(2,i):
            if i%j==0:
                result=False
        if result:
            slist.append(i)
    s=' '.join(map(str, slist))
    return s


print(testPrime())