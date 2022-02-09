num = 0
num2 = 1
num3 = 0
f = 0
c = 0
fibonacciSeq = []
while f < 1:
    print(num)
    while c < 25:
        print
        num3 = num + num2
        num = num2
        num2 = num3
        print(str(num))
        c += 1
        fibonacciSeq.append(num)
    f = 1


print(fibonacciSeq)

    #0,1,1,2,3,5,8