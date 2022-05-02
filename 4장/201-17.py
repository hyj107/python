# 201p 17번
for n in range(0,10,1):
    if n%3==0 and n%5==0:
        msg="fizzbuzz"
    elif n%3==0:
        msg="fizz"
    elif n%5==0:
        msg="buzz"
    else:
        msg="*"
    print(msg)